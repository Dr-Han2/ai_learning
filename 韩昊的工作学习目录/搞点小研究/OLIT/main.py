"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import numpy as np
import time

from OLIT import (generate_dag,generate_data,OLIT,is_topological_order,run_experiment)

#___________ 定义两个候选函数___________
def f_sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x / 2.0))

def f_cubic(x):
    # 论文中的 x^3 / |x|，即 sign(x) * x^2
    return np.sign(x) * x ** 2

def demo_single():
    n = 4
    N = 1000
    noise = "gaussian"
    seed = 42

    print("=" * 60)
    print(f"单次运行: n={n}, noise={noise}, N={N}")
    print("=" * 60)

    edges, topo_true = generate_dag(n, p=0.5, seed=seed)
    data = generate_data(edges, n, N=N, noise=noise, seed=seed + 1)

    print(f"真实边: {edges}")
    print(f"真实拓扑序: {topo_true}")

    t0 = time.time()
    pi, s, hist = OLIT(data, f=f_sigmoid, k=3, seed=seed + 2)
    t1 = time.time()

    print(f"OLIT 输出排列: {pi}")
    print(f"最终评分: {s:.4f}")
    print(f"评分历史: {[round(x, 4) for x in hist]}")
    print(f"是否为拓扑序: {is_topological_order(pi, edges)}")
    print(f"耗时: {t1 - t0:.2f}s")

# ============================================================
# 批量实验示例
# ============================================================
def demo_batch():
    print()
    print("=" * 60)
    print("批量实验: 不同 n 与噪声类型下的 OLIT 准确率")
    print("=" * 60)

    configs = [
        (2, "beta"),
        (2, "gaussian"),
        (2, "uniform"),
        (3, "beta"),
        (3, "gaussian"),
        (3, "uniform"),
    ]

    print(f"{'n':>3} {'noise':>10} {'accuracy':>10}")
    for n, noise in configs:
        acc = run_experiment(
            n=n,
            noise=noise,
            N=1000,
            f=f_sigmoid,
            k=3,
            n_trials=5,       # 演示用 5 次，正式复现可改 50
            base_seed=0,
        )
        print(f"{n:>3} {noise:>10} {acc:>10.3f}")

if __name__ == "__main__":
    demo_single()
    demo_batch()