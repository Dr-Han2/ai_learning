"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

np.random.seed(0)
torch.manual_seed(0)


# ============================================================
# 1. 冻结的 backbone（★ 加深加宽，特征更丰富）
# ============================================================
class FrozenBackbone(nn.Module):
    def __init__(self, in_dim=20, feat_dim=64):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, 128), nn.ReLU(),
            nn.Linear(128, 128), nn.ReLU(),
            nn.Linear(128, feat_dim)
        )
        for p in self.parameters():
            p.requires_grad = False

    def forward(self, x):
        return self.net(x)


# ============================================================
# 2. 每个任务的独立头（★ 升级为 2 层 MLP）—— 与 RLS 无关
# ============================================================
class TaskHead(nn.Module):
    def __init__(self, feat_dim, hidden=64, out_dim=1):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(feat_dim, hidden), nn.ReLU(),
            nn.Linear(hidden, out_dim)
        )

    def forward(self, f):
        return self.net(f)


# ============================================================
# 3. ★★★ RLS 路由器（核心，逻辑不变）★★★
# ============================================================
class RLSRouter:
    def __init__(self, feat_dim, n_tasks, lam=1.0, delta=1e3, verbose=False):
        self.W = np.zeros((feat_dim, n_tasks), dtype=np.float64)
        self.P = delta * np.eye(feat_dim, dtype=np.float64)
        self.lam = lam
        self.verbose = verbose
        self.step = 0

    def update(self, f, target):
        f = np.asarray(f, dtype=np.float64).reshape(-1, 1)
        target = np.asarray(target, dtype=np.float64).reshape(1, -1)

        # ---------- RLS 核心六步 ----------
        den = self.lam + (f.T @ self.P @ f).item()
        k = (self.P @ f) / den
        pred = f.T @ self.W
        alpha = target - pred
        self.W = self.W + k @ alpha
        self.P = (self.P - k @ f.T @ self.P) / self.lam
        self.P = (self.P + self.P.T) / 2.0
        self.P += 1e-8 * np.eye(self.P.shape[0])
        # ----------------------------------

        self.step += 1
        if self.verbose and self.step % 100 == 0:
            print(f"    [RLS step {self.step:4d}] "
                  f"|k|={np.linalg.norm(k):.4e}, "
                  f"|α|={np.linalg.norm(alpha):.4e}, "
                  f"tr(P)={np.trace(self.P):.4e}")

    def predict(self, f):
        return np.argmax(f @ self.W, axis=-1)


# ============================================================
# 4. 生成多任务数据（★ 任务分布差异更明显）
# ============================================================
def make_tasks(n_tasks=3, n_train=800, n_test=200, in_dim=20, seed=42):
    tasks = []
    for k in range(n_tasks):
        g = torch.Generator().manual_seed(seed + k)

        # 每个任务：
        #   - 均值偏移方向正交（用 one-hot 风格）
        #   - 投影矩阵不同
        #   - 回归系数不同
        mean = torch.zeros(in_dim)
        mean[k % in_dim] = 5.0                                # ★ 关键：沿不同坐标轴偏移
        proj = torch.randn(in_dim, in_dim, generator=g) * 0.5
        proj = proj + 2.0 * torch.eye(in_dim)                 # 加对角，保留原方向信息
        w = torch.randn(in_dim, 1, generator=g) * (k + 1)

        def make(n):
            X = torch.randn(n, in_dim, generator=g)
            X = X @ proj + mean
            y = X @ w + 0.1 * torch.randn(n, 1, generator=g)
            return X, y

        X_tr, y_tr = make(n_train)
        X_te, y_te = make(n_test)

        # ★ y 标准化（用训练集统计量）
        y_mean, y_std = y_tr.mean(), y_tr.std()
        y_tr = (y_tr - y_mean) / y_std
        y_te = (y_te - y_mean) / y_std

        tasks.append({
            "X_train": X_tr, "y_train": y_tr,
            "X_test": X_te, "y_test": y_te,
        })
    return tasks


# ============================================================
# 5. 评估工具
# ============================================================
def eval_task_mse(backbone, head, X, y):
    backbone.eval(); head.eval()
    with torch.no_grad():
        F = backbone(X)
        return torch.mean((head(F) - y) ** 2).item()


# ============================================================
# 6. 主流程
# ============================================================
def main():
    in_dim = 20
    feat_dim = 64
    n_tasks = 3
    n_epochs = 500
    lr = 5e-3
    hidden = 64

    backbone = FrozenBackbone(in_dim, feat_dim)
    heads = [TaskHead(feat_dim, hidden=hidden) for _ in range(n_tasks)]
    router = RLSRouter(feat_dim, n_tasks, lam=1.0, delta=1e3, verbose=True)

    tasks = make_tasks(n_tasks=n_tasks, n_train=800, n_test=200, in_dim=in_dim)

    print("=" * 60)
    print("顺序增量微调：任务 0 → 任务 1 → 任务 2")
    print("=" * 60)

    for k, task in enumerate(tasks):
        print(f"\n【任务 {k}】开始训练")
        X_tr, y_tr = task["X_train"], task["y_train"]
        head = heads[k]
        opt = optim.Adam(head.parameters(), lr=lr)
        sched = optim.lr_scheduler.CosineAnnealingLR(opt, T_max=n_epochs)
        loss_fn = nn.MSELoss()

        # ---------- 阶段 A：训练任务头（Adam + MSE） ----------
        head.train()
        for epoch in range(n_epochs):
            opt.zero_grad()
            loss = loss_fn(head(backbone(X_tr)), y_tr)
            loss.backward()
            opt.step()
            sched.step()

        train_mse = eval_task_mse(backbone, head, X_tr, y_tr)
        test_mse = eval_task_mse(backbone, head, task["X_test"], task["y_test"])
        print(f"  任务头训练完成: train MSE={train_mse:.6f}, test MSE={test_mse:.6f}")

        # ---------- 阶段 B：★ RLS 更新路由器 ★ ----------
        print(f"  开始 RLS 更新路由器（逐样本递推）...")
        with torch.no_grad():
            F_np = backbone(X_tr).numpy().astype(np.float64)
            for i in range(F_np.shape[0]):
                target = np.zeros(n_tasks)
                target[k] = 1.0
                router.update(F_np[i], target)

        # ---------- 阶段 C：评估所有已学任务（观察遗忘） ----------
        print(f"  P 条件数: {np.linalg.cond(router.P):.2e}")
        for j in range(k + 1):
            mse_j = eval_task_mse(
                backbone, heads[j],
                tasks[j]["X_test"], tasks[j]["y_test"]
            )
            print(f"    → 任务 {j} 测试 MSE = {mse_j:.6f}")

    # ---------- 最终测试 ----------
    print("\n" + "=" * 60)
    print("最终测试：路由准确率 + 任务 MSE")
    print("=" * 60)

    total_mse, total_n = 0.0, 0
    for k, task in enumerate(tasks):
        X_te, y_te = task["X_test"], task["y_test"]
        with torch.no_grad():
            F = backbone(X_te)
            F_np = F.numpy().astype(np.float64)
            pred_task = router.predict(F_np)
            acc = float(np.mean(pred_task == k))
            mse = torch.mean((heads[k](F) - y_te) ** 2).item()

        print(f"任务 {k}: 路由准确率={acc:.2%}, MSE={mse:.6f}")
        total_mse += mse * len(y_te)
        total_n += len(y_te)

    print(f"\n整体 MSE: {total_mse / total_n:.6f}")


if __name__ == "__main__":
    main()