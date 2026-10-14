"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

# 离散时间步长
Ts = 0.01

# %%%%%%%%%%%%%%%%% 参数设计 %%%%%%%%%%%%%%%%%
# 定义过程噪声协方差矩阵
Q = np.array([[0.01, 0.0],
              [0.0, 0.01]])
# 定义测量噪声协方差矩阵
R_c = np.array([[0.1, 0.0],
                [0.0, 0.1]])
# 定义重力加速度
g = 10.0
# 定义连杆长度
l = 0.5

# %%%%%%%%%%%%%%%%% 系统初始化 %%%%%%%%%%%%%%%%
# 初始化系统状态
x0 = np.array([np.pi / 4, 0.0])
# 初始化状态赋值
x = x0.copy()
# 初始化测量值
z0 = np.array([0.0, 0.0])
# 初始化测量值赋值
z = z0.copy()
# 初始化先验估计
x_hat_minus0 = np.array([0.0, 0.0])
# 初始化先验估计赋值
x_hat_minus = x_hat_minus0.copy()
# 初始化后验估计
x_hat0 = np.array([np.pi / 4, 0.0])
# 初始化后验估计赋值
x_hat = x_hat0.copy()
# 初始化后验估计误差协方差矩阵
P0 = np.array([[1.0, 0.0],
               [0.0, 1.0]])
# 初始后验估计误差协方差矩阵赋值
P = P0.copy()
# 计算变量维度
n = x.shape[0]

# 定义系统运行步数
k_steps = 200
# 定义历史记录矩阵（注意：循环中从 k+1 开始写入，因此列数为 k_steps+1）
x_history = np.zeros((n, k_steps + 1))
x_hat_history = np.zeros((n, k_steps + 1))
x_hat_minus_history = np.zeros((n, k_steps + 1))
z_history = np.zeros((n, k_steps + 1))

# %%%%%%%%%%%%% 生成过程与测量噪声 %%%%%%%%%%%%%%%%%%
Q_a = np.array([[0.1, 0.0],
                [0.0, 0.1]])
# 定义真实的测量噪声协方差矩阵
R_a = np.array([[0.1, 0.0],
                [0.0, 0.1]])
# 随机生成过程噪声（与 MATLAB 中 chol 行为一致，对角矩阵下 L = chol 结果相同）
w = np.linalg.cholesky(Q_a) @ np.random.randn(2, k_steps)
# 随机生成测量噪声
v = np.sqrt(R_a) @ np.random.randn(2, k_steps)

# %% Kalman Filter
for k in range(k_steps):
    # 系统状态空间方程，计算实际状态变量 x1
    x[0] = x[0] + x[1] * Ts + w[0, k]
    # 系统状态空间方程，计算实际状态变量 x2
    x[1] = x[1] - g / l * np.sin(x[0]) * Ts + w[1, k]
    # 计算实际测量值，在实际应用中，这一项来自传感器测量
    z[0] = x[0] + v[0, k]
    z[1] = x[1] + v[1, k]

    # %%%%%%%%%%%%%%%%%% 扩展卡尔曼滤波器 %%%%%%%%%%%%%%%%%
    # 计算先验状态估计
    x_hat_minus[0] = x_hat[0] + x_hat[1] * Ts
    x_hat_minus[1] = x_hat[1] - g / l * np.sin(x_hat[0]) * Ts
    # 计算更新雅可比矩阵
    A = np.array([[1.0, Ts],
                  [-g / l * np.cos(x_hat[0]) * Ts, 1.0]])
    W = np.array([[1.0, 0.0],
                  [0.0, 1.0]])
    H_m = np.array([[1.0, 0.0],
                    [0.0, 1.0]])
    V = np.array([[1.0, 0.0],
                  [0.0, 1.0]])
    # 计算先验估计误差协方差矩阵
    P_minus = A @ P @ A.T + W.T @ Q @ W
    # 计算卡尔曼增益
    K = P_minus @ H_m.T @ np.linalg.inv(H_m @ P_minus @ H_m.T + V @ R_c @ V.T)
    # 更新后验估计
    x_hat = x_hat_minus + K @ (z - x_hat_minus)
    # 后验估计误差协方差矩阵
    P = (np.eye(n) - K @ H_m) @ P_minus
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    # 保存系统状态到预先定义矩阵的相应位置
    x_history[:, k + 1] = x
    # 保存测量值到预先定义矩阵的相应位置
    z_history[:, k + 1] = z
    # 保存先验估计到预先定义矩阵的相应位置
    x_hat_minus_history[:, k + 1] = x_hat_minus
    # 保存后验估计到预先定义矩阵的相应位置
    x_hat_history[:, k + 1] = x_hat

# %%%%%%%%%%%%%%%%% 结果 %%%%%%%%%%%%%%%%%%%%%%%%%%%
fig = plt.figure(figsize=(15, 5))
t = np.arange(x_history.shape[1])

# x1 真实结果
plt.plot(t, x_history[0, :], '--', linewidth=2, label='真实值')
# x1 测量值
plt.plot(t, z_history[0, :], '*', markersize=8, label='测量值')
# x1 先验估计值
plt.plot(t, x_hat_minus_history[0, :], 'o', markersize=8, label='先验估计值')
# x1 后验估计值
plt.plot(t, x_hat_history[0, :], linewidth=2, label='后验估计值')

plt.ylim([-3, 3])
plt.legend(loc='lower right', fontsize=20)
plt.grid(True)
plt.show()

# 计算 Ems 均方误差
diff = x_hat_history[0, :] - x_history[0, :]
Ems = diff @ diff.T / k_steps
print("Ems =", Ems)