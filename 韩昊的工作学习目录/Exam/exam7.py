"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
"""
大模型增量微调：RLS 路由器 + 独立 LoRA 头 的极简实现

设计要点：
1. FrozenBackbone  —— 模拟大模型底座，物理隔离，参数永不更新
2. TaskHead        —— 模拟每个任务的独立 LoRA 子空间
3. RLSRouter       —— 在线二阶优化器，快速学习任务归属
4. 遗忘因子 λ       —— 控制路由器对新任务的适应速度（不保护旧参数）
"""
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
from dataclasses import dataclass
from typing import List, Tuple

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim


# ============================================================
# 0. 配置
# ============================================================
@dataclass
class Config:
    in_dim: int = 20
    feat_dim: int = 32
    n_tasks: int = 3
    n_samples_per_task: int = 200

    head_epochs: int = 100
    head_lr: float = 1e-2

    rls_lambda: float = 1.0     # 遗忘因子 λ∈(0,1]，1.0 表示不遗忘
    rls_delta: float = 1.0      # P 的初始化尺度

    seed: int = 0


# ============================================================
# 1. 冻结特征提取器（模拟大模型底层）
# ============================================================
class FrozenBackbone(nn.Module):
    def __init__(self, in_dim: int, feat_dim: int):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, 64),
            nn.ReLU(),
            nn.Linear(64, feat_dim),
        )
        for p in self.parameters():
            p.requires_grad = False

    @torch.no_grad()
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


# ============================================================
# 2. 每个任务的独立头（模拟 LoRA）
# ============================================================
class TaskHead(nn.Module):
    def __init__(self, feat_dim: int, out_dim: int = 1):
        super().__init__()
        self.fc = nn.Linear(feat_dim, out_dim)

    def forward(self, f: torch.Tensor) -> torch.Tensor:
        return self.fc(f)


# ============================================================
# 3. RLS 路由器（稳健 1-D 版本）
# ============================================================
class RLSRouter:
    """
    递归最小二乘（RLS）实现多分类路由。

    - W: (feat_dim, n_tasks)          权重
    - P: (feat_dim, feat_dim)         逆相关矩阵（近似二阶信息）
    - λ: 遗忘因子，λ<1 时旧样本影响指数衰减
    """

    def __init__(self, feat_dim: int, n_tasks: int,
                 lam: float = 1.0, delta: float = 1.0):
        assert 0.0 < lam <= 1.0, "λ 必须落在 (0, 1]"
        self.W = np.zeros((feat_dim, n_tasks), dtype=np.float64)
        self.P = delta * np.eye(feat_dim, dtype=np.float64)
        self.lam = float(lam)
        self.feat_dim = feat_dim
        self.n_updates = 0

    def update(self, f: np.ndarray, target: np.ndarray) -> None:
        """f: (feat_dim,), target: (n_tasks,) one-hot"""
        f = np.asarray(f, dtype=np.float64).ravel()          # (D,)
        target = np.asarray(target, dtype=np.float64).ravel()  # (T,)

        Pf = self.P @ f                     # (D,)
        den = self.lam + f @ Pf             # 标量
        k = Pf / den                        # (D,)

        pred = f @ self.W                   # (T,)
        self.W += np.outer(k, target - pred)  # (D, T)

        # Joseph 形式 + 对称化
        I_kf = np.eye(self.feat_dim) - np.outer(k, f)
        self.P = (I_kf @ self.P) / self.lam
        self.P = 0.5 * (self.P + self.P.T)

        self.n_updates += 1

    def predict(self, f: np.ndarray) -> np.ndarray:
        f = np.asarray(f, dtype=np.float64)
        single = f.ndim == 1
        f2 = f.reshape(1, -1) if single else f       # (N, D)
        logits = f2 @ self.W                          # (N, T)
        idx = np.argmax(logits, axis=-1)              # (N,)
        return int(idx[0]) if single else idx

    def predict_proba(self, f: np.ndarray) -> np.ndarray:
        f = np.asarray(f, dtype=np.float64)
        single = f.ndim == 1
        f2 = f.reshape(1, -1) if single else f
        logits = f2 @ self.W
        logits = logits - logits.max(axis=-1, keepdims=True)
        exp = np.exp(logits)
        proba = exp / exp.sum(axis=-1, keepdims=True)
        return proba[0] if single else proba


# ============================================================
# 4. 数据生成
# ============================================================
def generate_task_data(n_tasks: int, n_samples: int, in_dim: int,
                       seed: int = 0) -> List[Tuple[torch.Tensor, torch.Tensor]]:
    g = torch.Generator().manual_seed(seed)
    tasks = []
    for k in range(n_tasks):
        X = torch.randn(n_samples, in_dim, generator=g)
        true_w = torch.randn(in_dim, 1, generator=g) * (k + 1)
        y = X @ true_w + 0.1 * torch.randn(n_samples, 1, generator=g)
        tasks.append((X, y))
    return tasks


# ============================================================
# 5. 单任务头训练（backbone 冻结 -> 特征可预计算）
# ============================================================
def train_one_task(backbone: nn.Module, head: nn.Module,
                   X: torch.Tensor, y: torch.Tensor,
                   epochs: int, lr: float) -> Tuple[torch.Tensor, float]:
    with torch.no_grad():
        F = backbone(X)            # 只算一次

    optimizer = optim.Adam(head.parameters(), lr=lr)
    loss_fn = nn.MSELoss()
    loss_val = 0.0
    for _ in range(epochs):
        optimizer.zero_grad()
        loss = loss_fn(head(F), y)
        loss.backward()
        optimizer.step()
        loss_val = loss.item()

    with torch.no_grad():
        F = backbone(X)            # 保证与最终参数一致
    return F, loss_val


# ============================================================
# 6. 评估
# ============================================================
def evaluate(tasks, backbone, task_heads, router, n_tasks):
    print("\n=== 测试结果 ===")
    total_sse_oracle, total_sse_routed, total_n = 0.0, 0.0, 0

    for k, (X, y) in enumerate(tasks):
        with torch.no_grad():
            F = backbone(X)
        F_np = F.numpy()

        routed = router.predict(F_np)
        acc = float(np.mean(routed == k))

        # Oracle 路由：直接用 task_heads[k]，衡量"隔离"本身的保真度
        with torch.no_grad():
            y_oracle = task_heads[k](F).numpy()
        mse_oracle = float(np.mean((y.numpy() - y_oracle) ** 2))

        # 真实路由：按路由器判决选 head
        y_routed = np.zeros_like(y.numpy())
        for i in range(len(X)):
            with torch.no_grad():
                pred_i = task_heads[int(routed[i])](F[i:i + 1]).numpy().ravel()
                y_routed[i] = pred_i

        mse_routed = float(np.mean((y.numpy() - y_routed) ** 2))
        conf = float(np.mean(router.predict_proba(F_np).max(axis=-1)))

        print(f"任务 {k}: 路由acc={acc:.2%} | conf={conf:.3f} | "
              f"MSE(oracle)={mse_oracle:.4f} | MSE(routed)={mse_routed:.4f}")

        total_sse_oracle += float(np.sum((y.numpy() - y_oracle) ** 2))
        total_sse_routed += float(np.sum((y.numpy() - y_routed) ** 2))
        total_n += len(y)

    print(f"\n整体 MSE(oracle 路由) : {total_sse_oracle / total_n:.4f}")
    print(f"整体 MSE(RLS 路由)    : {total_sse_routed / total_n:.4f}")


# ============================================================
# 7. 主流程
# ============================================================
def main(cfg: Config = Config()):
    # 统一种子
    torch.manual_seed(cfg.seed)
    np.random.seed(cfg.seed)

    backbone = FrozenBackbone(cfg.in_dim, cfg.feat_dim)
    task_heads = [TaskHead(cfg.feat_dim) for _ in range(cfg.n_tasks)]
    router = RLSRouter(cfg.feat_dim, cfg.n_tasks,
                       lam=cfg.rls_lambda, delta=cfg.rls_delta)

    tasks = generate_task_data(cfg.n_tasks, cfg.n_samples_per_task,
                               cfg.in_dim, seed=cfg.seed)

    # ---- 顺序增量训练 ----
    for k, (X, y) in enumerate(tasks):
        F, loss_val = train_one_task(
            backbone, task_heads[k], X, y,
            epochs=cfg.head_epochs, lr=cfg.head_lr,
        )
        F_np = F.numpy()
        for i in range(len(X)):
            target = np.zeros(cfg.n_tasks)
            target[k] = 1.0
            router.update(F_np[i], target)

        print(f"[任务 {k}] head loss={loss_val:.4f} | "
              f"router updates={router.n_updates}")

    # ---- 评估 ----
    evaluate(tasks, backbone, task_heads, router, cfg.n_tasks)
    return backbone, task_heads, router, tasks


if __name__ == "__main__":
    # 对比：λ=1.0（不遗忘） vs λ=0.95（快速适应）
    print("=" * 60)
    print("实验 1: λ = 1.0 （不遗忘，稳定优先）")
    print("=" * 60)
    main(Config(rls_lambda=1.0))

    print("\n" + "=" * 60)
    print("实验 2: λ = 0.95 （遗忘因子 < 1，快速追踪）")
    print("=" * 60)
    main(Config(rls_lambda=0.95))