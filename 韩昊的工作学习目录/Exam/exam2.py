"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""

# 需要: numpy, torch
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import numpy as np, torch

# 判 PD：Cholesky 成功即 PD；失败则非 PD
def is_pd_numpy(A):
    try:
        np.linalg.cholesky(A)
        return True
    except np.linalg.LinAlgError:
        return False

A = np.array([[2., 1.], [1., 3.]])
print("PD? ", is_pd_numpy(A))  # True

# 马氏距离
mu = np.array([0., 0.])
Sigma = np.array([[1., 0.], [0., 9.]])
x = np.array([1., 3.])
d2 = (x - mu).T @ np.linalg.inv(Sigma) @ (x - mu)
print("Mahalanobis^2 =", d2)

# PyTorch 版: 用 cholesky_solve 更稳
At = torch.tensor(A)                        # float64
L = torch.linalg.cholesky(At)               # float64
b = torch.tensor([1., 0.], dtype=L.dtype)   # ← 关键：跟随 L 的 dtype
y = torch.cholesky_solve(b.reshape(-1, 1), L).squeeze()
print("Solve Ay=b -> y=", y)

