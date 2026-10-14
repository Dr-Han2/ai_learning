"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import numpy as np
from scipy.optimize import minimize

# 1. 定义负对数似然函数（因为scipy只有求最小值的函数，所以求负值的极小值等价于求原函数极大值）
def neg_log_likelihood(p, y):
    # 加入微小量 1e-10 防止 log(0) 报错
    return -np.sum(y * np.log(p + 1e-10))

# 2. 设置约束：p0 + p1 + p2 = 1
cons = ({'type': 'eq', 'fun': lambda p: np.sum(p) - 1})

# 3. 设置参数范围：0 <= p <= 1
bounds = ((0, 1), (0, 1), (0, 1))

# 4. 初始猜测值
p_init = [1/3, 1/3, 1/3]

# 5. 数据输入
y_data = np.array([39, 37, 44])

# 6. 进行优化
res = minimize(neg_log_likelihood, p_init, args=(y_data,), bounds=bounds, constraints=cons)

print("优化成功:", res.success)
print(f"优化求得的最优值: p0={res.x[0]:.4f}, p1={res.x[1]:.4f}, p2={res.x[2]:.4f}")