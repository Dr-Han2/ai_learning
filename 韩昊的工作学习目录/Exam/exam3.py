import numpy as np

def pca_svd(X, k):
    # X: (m, d), 行为样本；先中心化
    Xc = X - X.mean(axis=0, keepdims=True)
    U, S, Vt = np.linalg.svd(Xc, full_matrices=False)  # Xc = U Σ V^T
    Vk = Vt[:k].T             # (d, k)
    Z  = Xc @ Vk              # (m, k) 低维表示
    evr = (S**2) / (X.shape[0] * (S**2).sum())  # 每个成分解释方差比
    return Z, Vk, evr

# demo
X = np.random.randn(500, 64)
Z, Vk, evr = pca_svd(X, k=10)
print("Z shape:", Z.shape, "EVR first 3:", evr[:3].round(3))