"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

import time
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np


# ============================================================
# 1. 冻结特征提取器（模拟大模型底层）
# ============================================================
class FrozenBackbone(nn.Module):
    def __init__(self, in_dim=20, feat_dim=32):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, 64),
            nn.ReLU(),
            nn.Linear(64, feat_dim)
        )
        for p in self.parameters():
            p.requires_grad = False

    def forward(self, x):
        return self.net(x)


# ============================================================
# 2. 每个任务的独立头（模拟 LoRA）—— ★ 升级为 2 层 MLP
# ============================================================
class TaskHead(nn.Module):
    def __init__(self, feat_dim, hidden=64, out_dim=1):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(feat_dim, hidden),
            nn.ReLU(),
            nn.Linear(hidden, out_dim)
        )

    def forward(self, f):
        return self.net(f)


# ============================================================
# 3. RLS 路由器
# ============================================================
class RLSRouter:
    def __init__(self, feat_dim, n_tasks, lam=1.0, delta=1e3, jitter=1e-8):
        self.W = np.zeros((feat_dim, n_tasks), dtype=np.float64)
        self.P = delta * np.eye(feat_dim, dtype=np.float64)
        self.lam = float(lam)
        self.jitter = float(jitter)

    def update(self, f, target):
        f = np.asarray(f, dtype=np.float64).reshape(-1, 1)
        target = np.asarray(target, dtype=np.float64).reshape(1, -1)

        den = self.lam + (f.T @ self.P @ f).item()
        if den < 1e-12:
            den = 1e-12

        k = (self.P @ f) / den
        pred = f.T @ self.W
        self.W = self.W + k @ (target - pred)

        self.P = (self.P - k @ f.T @ self.P) / self.lam
        self.P = (self.P + self.P.T) / 2.0
        self.P = self.P + self.jitter * np.eye(self.P.shape[0])

    def predict(self, f):
        f = np.asarray(f, dtype=np.float64)
        return np.argmax(f @ self.W, axis=-1)

    def condition_number(self):
        return float(np.linalg.cond(self.P))


# ============================================================
# 4. 生成任务数据（★ 每个任务独立分布 + y 标准化）
# ============================================================
def generate_task_data(n_tasks, n_train, n_test, in_dim=20, base_seed=0):
    """
    每个任务：
      - 独立输入均值 task_mean
      - 独立线性变换 task_proj
      - 独立回归系数 true_w
      - ★ 对 y 做 z-score 标准化（用训练集统计量），使 MSE 落在噪声量级
    """
    tasks = []
    for k in range(n_tasks):
        g = torch.Generator().manual_seed(base_seed + k)

        task_mean = torch.randn(in_dim, generator=g) * 2.0
        task_proj = torch.randn(in_dim, in_dim, generator=g)
        true_w = torch.randn(in_dim, 1, generator=g) * (k + 1)

        def make(n):
            X = torch.randn(n, in_dim, generator=g)
            X = X @ task_proj + task_mean
            y = X @ true_w + 0.1 * torch.randn(n, 1, generator=g)
            return X, y

        X_train, y_train = make(n_train)
        X_test, y_test = make(n_test)

        # ★ y 标准化：用训练集统计量
        y_mean = y_train.mean()
        y_std = y_train.std()
        y_train = (y_train - y_mean) / y_std
        y_test = (y_test - y_mean) / y_std

        tasks.append({
            "X_train": X_train, "y_train": y_train,
            "X_test": X_test, "y_test": y_test,
        })
    return tasks


# ============================================================
# 5. 工具函数
# ============================================================
def eval_task_mse(backbone, head, X, y, device):
    backbone.eval()
    head.eval()
    with torch.no_grad():
        X, y = X.to(device), y.to(device)
        F = backbone(X)
        y_pred = head(F)
        mse = torch.mean((y_pred - y) ** 2).item()
    return mse


# ============================================================
# 6. 顺序增量训练
# ============================================================
def main():
    # ---------- 超参数 ----------
    in_dim = 20
    feat_dim = 32
    n_tasks = 3
    n_train = 500
    n_test = 200
    n_epochs = 300
    lr = 5e-3
    hidden = 64

    torch.manual_seed(0)
    np.random.seed(0)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"使用设备: {device}")

    # ---------- 模型与路由器 ----------
    backbone = FrozenBackbone(in_dim, feat_dim).to(device)
    task_heads = [TaskHead(feat_dim, hidden=hidden).to(device) for _ in range(n_tasks)]
    router = RLSRouter(feat_dim, n_tasks, lam=1.0, delta=1e3)

    tasks = generate_task_data(n_tasks, n_train, n_test, in_dim, base_seed=42)

    # ---------- 顺序训练 ----------
    t_start = time.time()
    print("\n=== 顺序增量训练 ===")
    for k, task in enumerate(tasks):
        X_tr, y_tr = task["X_train"].to(device), task["y_train"].to(device)
        head = task_heads[k]
        optimizer = optim.Adam(head.parameters(), lr=lr)
        scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=n_epochs)
        loss_fn = nn.MSELoss()

        # 训练当前任务头
        head.train()
        for epoch in range(n_epochs):
            optimizer.zero_grad()
            F = backbone(X_tr)
            pred = head(F)
            loss = loss_fn(pred, y_tr)
            loss.backward()
            optimizer.step()
            scheduler.step()

        train_mse = eval_task_mse(backbone, head, X_tr, y_tr, device)
        test_mse = eval_task_mse(backbone, head, task["X_test"], task["y_test"], device)

        # 用 RLS 增量更新路由器
        head.eval()
        with torch.no_grad():
            F_np = backbone(X_tr).detach().cpu().numpy().astype(np.float64)
            for i in range(F_np.shape[0]):
                target = np.zeros(n_tasks, dtype=np.float64)
                target[k] = 1.0
                router.update(F_np[i], target)

        print(f"\n任务 {k} 完成: train MSE={train_mse:.6f}, "
              f"test MSE={test_mse:.6f}, P 条件数={router.condition_number():.2e}")

        # 立刻在所有已学任务上评估（观察遗忘）
        for j in range(k + 1):
            mse_j = eval_task_mse(
                backbone, task_heads[j],
                tasks[j]["X_test"], tasks[j]["y_test"], device
            )
            print(f"  → 任务 {j} 测试 MSE = {mse_j:.6f}")

    t_train = time.time() - t_start

    # ---------- 最终测试 ----------
    print("\n=== 最终测试结果 ===")
    total_mse = 0.0
    total_n = 0

    for k, task in enumerate(tasks):
        X_te, y_te = task["X_test"].to(device), task["y_test"].to(device)
        with torch.no_grad():
            F = backbone(X_te)                                   # 保持 float32
            F_np = F.detach().cpu().numpy().astype(np.float64)   # 路由器用 float64
            pred_task = router.predict(F_np)
            acc = float(np.mean(pred_task == k))

            y_pred = task_heads[k](F)
            mse = torch.mean((y_pred - y_te) ** 2).item()

        print(f"任务 {k}: 路由准确率={acc:.2%}, MSE={mse:.6f}")
        total_mse += mse * y_te.shape[0]
        total_n += y_te.shape[0]

    print(f"\n整体 MSE: {total_mse / total_n:.6f}")
    print(f"训练总耗时: {t_train:.2f}s")


if __name__ == "__main__":
    main()