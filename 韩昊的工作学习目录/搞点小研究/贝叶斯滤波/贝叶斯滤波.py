"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#python

import numpy as np

#状态0 表示A 状态1 表示B
#初始先验
prior = np.array([0.5, 0.5]) #[P(A), P(B)]

#转移矩阵 T[i, j] = P(x_t=i | x_{t-1} = j)

T = np.array([
    [0.6, 0.4],  # P(A|A), P(A|B)
    [0.4, 0.6]   # P(B|A), P(B|B)
])
print(f"转移矩阵是:",T)

#观测序列O_A, O_A, O_B
observations = ['O_A', 'O_A', 'O_B']

#似然
likelihood_dict ={
    'O_A': np.array([0.8, 0.2]),# P(O_A|A), P(O_A|B)
    'O_B': np.array([0.2, 0.8])# P(O_B|A), P(O_B|B),

}

print("初始先验:", prior)

for t, obs in enumerate(observations, start=1):
    print(f"\n--- 时间步 {t}，观测：{obs} ---")

    # 1. 预测
    predicted = T @ prior
    print("预测分布：", np.round(predicted, 4))

    # 2. 更新
    likelihood = likelihood_dict[obs]
    posterior = likelihood * predicted
    posterior = posterior / posterior.sum()
    print("更新后验：", np.round(posterior, 4))

    # 后验作为下一步先验
    prior = posterior

# 最终估计
estimated_state = np.argmax(prior)
state_name = 'A' if estimated_state == 0 else 'B'
print(f"\n最终估计状态：{state_name}，概率：{prior[estimated_state]:.4f}")


