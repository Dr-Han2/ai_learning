"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import numpy as np
import matplotlib.pyplot as plt
from OLIT import generate_dag, generate_data, OLIT

n = 4
edges, _ = generate_dag(n, p=0.5, seed=42)
data = generate_data(edges, n, N=1000, noise="gaussian", seed=43)

f = lambda x: 1.0 / (1.0 + np.exp(-x / 2.0))
pi, score, history = OLIT(data, f=f, k=3, seed=44)

plt.plot(history, marker="o")
plt.xlabel("iteration")
plt.ylabel("score")
plt.title("OLIT score history")
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("olit_score_history.png", dpi=150)
plt.show()