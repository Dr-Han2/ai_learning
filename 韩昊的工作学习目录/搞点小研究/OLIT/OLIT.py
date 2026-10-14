"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import numpy as np
from collections import defaultdict, deque
from scipy.special import digamma, gamma
from sklearn.neighbors import NearestNeighbors
import random

#============================
# 1 随机生成一个DAG(有向无环图)
#============================
def generate_dag(n, p=0.5, seed=None):
    """
         使用 Erdos-Renyi 边概率模型生成随机DAG。
         先随机生成一个拓扑序,再只允许从前往后加边,保证无环
        """
    rng = np.random.default_rng(seed)
    topo_order = list(rng.permutation(n))
    pos = {node: idx for idx, node in enumerate(topo_order)}

    edges = []
    for i in range(n):
        for j in range(n):
            if pos[i] < pos[j] and rng.random() < p:
                edges.append((i, j))

    return edges, topo_order


#============================
# 2 线性 SEM 数据生成
#============================
def generate_data(edges, n, N=1000, noise="gaussian", seed=None):
    """
    按线性 SEM 生成数据:
        X_j = sum_{i in Pa(X_j)} w_{ij} X_i + eps_j

    边权重从 [-1, -0.25] U [0.25, 1] 均匀采样。
    噪声类型: 'gaussian' | 'uniform' | 'beta'
    """
    rng = np.random.default_rng(seed)

    # 拓扑排序
    adj = defaultdict(list)
    indeg = [0] * n
    for i, j in edges:
        adj[i].append(j)
        indeg[j] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    # 边权重
    W = np.zeros((n, n))
    for i, j in edges:
        sign = rng.choice([-1, 1])
        W[i, j] = sign * rng.uniform(0.25, 1.0)

    # 每个节点的噪声参数（每个节点独立采样一次）
    noise_cfg = []
    for _ in range(n):
        if noise == "gaussian":
            mean = 0.0
            std = np.sqrt(rng.uniform(0.5, 2.0))
            noise_cfg.append(("gaussian", mean, std))
        elif noise == "uniform":
            low = 0.0
            high = rng.uniform(0.5, 2.0)
            noise_cfg.append(("uniform", low, high))
        elif noise == "beta":
            a = rng.uniform(0.5, 2.0)
            b = rng.uniform(0.5, 2.0)
            noise_cfg.append(("beta", a, b))
        else:
            raise ValueError(f"未知噪声类型: {noise}")

    def sample_noise(cfg):
        kind = cfg[0]
        if kind == "gaussian":
            return rng.normal(cfg[1], cfg[2])
        elif kind == "uniform":
            return rng.uniform(cfg[1], cfg[2])
        elif kind == "beta":
            return rng.beta(cfg[1], cfg[2])

    data = np.zeros((N, n))
    for node in topo:
        parents = [i for i in range(n) if W[i, node] != 0]
        eps = np.array([sample_noise(noise_cfg[node]) for _ in range(N)])
        if parents:
            data[:, node] = data[:, parents] @ W[parents, node] + eps
        else:
            data[:, node] = eps
    return data


#============================
# 3 k-NN 熵估计
#============================
def entropy_knn(X, k=3):
    """
    k-NN 微分熵估计.
    X：shape(N,) or (N, d)
    """
    X = np.asarray(X, dtype=float)
    if X.ndim == 1:
        X = X.reshape(-1, 1)
    N, d = X.shape
    if N <= k:
        raise ValueError(f"样本数太少: N={N}, k={k}")

    nbrs = NearestNeighbors(n_neighbors=k + 1).fit(X)
    distances, _ = nbrs.kneighbors(X)
    eps = distances[:, k]  # 第 k 个近邻距离
    eps = np.maximum(eps, 1e-12)  # 防止 log(0)

    c_d = np.pi ** (d / 2.0) / gamma(d / 2.0 + 1.0)  # d 维单位球体积
    H = digamma(N) - digamma(k) + np.log(c_d) + d * np.mean(np.log(eps))
    return float(H)

def conditional_entropy_knn(X, Y, k=3):
    """
    H(X | Y) = H(X, Y) - H(Y)
    X: (N,) 或 (N, d1); Y: (N,) 或 (N, d2)
    """
    X = np.asarray(X, dtype=float)
    Y = np.asarray(Y, dtype=float)
    if X.ndim == 1:
        X = X.reshape(-1, 1)
    if Y.ndim == 1:
        Y = Y.reshape(-1, 1)
    XY = np.hstack([X, Y])
    return entropy_knn(XY, k) - entropy_knn(Y, k)

#============================
# 4 构建评分函数
#============================
def make_score(data, f, k=3):
    """
    s(pi)= -sum_{t=1}^{n} f(H(X_{i_t}|X_{i_1},...X_{i_t-1}))
    data : shape(N, n)
    """
    n = data.shape[1]

    def score(pi):
        total = 0.0
        for pos, node in enumerate(pi):
            X_node = data[:, node]
            if pos == 0:
                H = entropy_knn(X_node, k)
            else:
                Y = data[:, list(pi[:pos])]
                H = conditional_entropy_knn(X_node, Y, k)
            total += f(H)
        return -total

    return score


# ============================================================
# 5. 插入变换
# ============================================================
def insert_transform(pi, u, v):
    """
    将 pi 中第 u 个元素移动到第 v 个元素之后 (0-based, u < v)。
    返回新的 list。
    """
    x = pi[u]
    new_pi = pi[:u] + pi[u + 1 : v + 1] + [x] + pi[v + 1 :]
    return new_pi


# ============================================================
# 6. OLIT 主算法
# ============================================================
def OLIT(data, f, k=3, initial_pi=None, max_iter=1000, seed=None):
    """
    OLIT 贪心搜索。

    参数:
        data: (N, n) ndarray
        f: 一元函数
        k: k-NN 的 k
        initial_pi: 初始排列（None 表示随机）
        max_iter: 最大迭代轮数
        seed: 随机种子

    返回:
        pi: 学到的排列
        current_score: 最终评分
        history: 每轮评分列表
    """
    n = data.shape[1]
    score = make_score(data, f, k)

    if initial_pi is None:
        rng = np.random.default_rng(seed)
        pi = list(rng.permutation(n))
    else:
        pi = list(initial_pi)

    current_score = score(pi)
    history = [current_score]

    for _ in range(max_iter):
        best_pi = pi
        best_score = current_score
        for u in range(n):
            for v in range(u + 1, n):
                cand = insert_transform(pi, u, v)
                s = score(cand)
                if s > best_score:
                    best_score = s
                    best_pi = cand
        if best_score > current_score:
            pi = best_pi
            current_score = best_score
            history.append(current_score)
        else:
            break

    return pi, current_score, history


# ============================================================
# 7. 评估工具
# ============================================================
def is_topological_order(pi, edges):
    """判断 pi 是否是 edges 对应 DAG 的一个拓扑序。"""
    pos = {node: idx for idx, node in enumerate(pi)}
    for i, j in edges:
        if pos[i] > pos[j]:
            return False
    return True


def run_experiment(n, noise, N=1000, f=None, k=3, n_trials=10, base_seed=0):
    """
    批量实验: 返回 OLIT 的准确率。
    """
    if f is None:
        f = lambda x: 1.0 / (1.0 + np.exp(-x / 2.0))

    correct = 0
    for t in range(n_trials):
        seed = base_seed + t * 100
        edges, _ = generate_dag(n, p=0.5, seed=seed)
        data = generate_data(edges, n, N=N, noise=noise, seed=seed + 1)
        pi, _, _ = OLIT(data, f=f, k=k, seed=seed + 2)
        if is_topological_order(pi, edges):
            correct += 1
    return correct / n_trials






