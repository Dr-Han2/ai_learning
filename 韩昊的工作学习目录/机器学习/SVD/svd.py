"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import numpy as np
import matplotlib.pyplot as plt

m, n = 300, 400
x = np.linspace(-1, 1, n)
y = np.linspace(-1, 1, m)
X,Y =np.meshgrid(x, y)

A = np.sin(10 * X) * np.cos(10 * Y) +0.5 * np.sin(20 *X * Y)

U, s, Vt = np.linalg.svd(A,full_matrices=False)

print("奇异值数量:",len(s))
print("前10个奇异值:",s[:10])

k = 50
A_k =U[:, :k] @ np.diag(s[:k]) @ Vt[:k, :]

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(A, cmap='gray')
plt.title('原矩阵')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(A_k, cmap='gray')
plt.title(f'前 {k} 个奇异值重建')
plt.axis('off')

plt.tight_layout()
plt.show()

orig = m * n
comp = k * (m + n + 1)   # U: m*k, s: k, Vt: k*n

print(f"原始存储量：{orig}")
print(f"压缩后存储量：{comp}")
print(f"压缩比：{orig / comp:.2f}")