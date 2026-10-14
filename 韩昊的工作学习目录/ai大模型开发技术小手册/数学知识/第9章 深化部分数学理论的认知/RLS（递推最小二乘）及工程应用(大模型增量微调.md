# RLS（递推最小二乘法) 

## 1. 解决什么问题

RLS 算法的目标是：**在每个时间点 $n$，找到一组滤波器系数 $w(n)$，使得从初始时刻到当前时刻的加权误差平方和最小。**

误差定义为：

$$
e(n)=d(n)-y(n)
$$

其中：

- $d(n)$：期望信号
- $x(n)$：输入向量/回归向量
- $w(n)$：滤波器系数
- $y(n)=x^T(n)w(n)$：滤波器输出

因此误差也可写为：

$$
e(n)=d(n)-x^T(n)w(n)
$$

RLS 通过引入遗忘因子 $\lambda$（通常 $0<\lambda\le 1$，非平稳时常取 $0<\lambda<1$）对过去的数据进行指数加权，使越旧的数据权重越小，从而能够跟踪非平稳信号的统计特性。

目标函数为：

$$
\min_{w(n)} J(n)=\sum_{i=1}^{n}\lambda^{n-i}
\left[d(i)-x^T(i)w(n)\right]^2
$$

---

## 2. 解答推导

### 2.1 加权最小二乘与正规方程

对目标函数 $J(n)$ 关于 $w(n)$ 求导并令其为零：

$$
\frac{\partial J(n)}{\partial w(n)}
=
-2\sum_{i=1}^{n}\lambda^{n-i}x(i)
\left[d(i)-x^T(i)w(n)\right]
=
0
$$

整理得到正规方程：

$$
\left(
\sum_{i=1}^{n}\lambda^{n-i}x(i)x^T(i)
\right)w(n)
=
\sum_{i=1}^{n}\lambda^{n-i}x(i)d(i)
$$

定义加权自相关矩阵：

$$
R(n)=\sum_{i=1}^{n}\lambda^{n-i}x(i)x^T(i)
$$

定义加权互相关向量：

$$
p(n)=\sum_{i=1}^{n}\lambda^{n-i}x(i)d(i)
$$

于是：

$$
R(n)w(n)=p(n)
$$

因此：

$$
w(n)=R^{-1}(n)p(n)
$$

令：

$$
P(n)=R^{-1}(n)
$$

则 $P(n)$ 可理解为参数估计的协方差矩阵，表示参数不确定性。

---

### 2.2 递推关系

加入新数据 $x(n),d(n)$ 后：

$$
R(n)=\lambda R(n-1)+x(n)x^T(n)
$$

$$
p(n)=\lambda p(n-1)+x(n)d(n)
$$

直接求 $R^{-1}(n)$ 计算量大，因此使用矩阵求逆引理递推更新 $P(n)$。

---

### 2.3 协方差矩阵递推

由 $P(n)=R^{-1}(n)$，有：

$$
P(n)=\left(\lambda R(n-1)+x(n)x^T(n)\right)^{-1}
$$

应用矩阵求逆引理：

$$
(A+BCD)^{-1}
=
A^{-1}
-
A^{-1}B
\left(C^{-1}+DA^{-1}B\right)^{-1}
DA^{-1}
$$

令：

$$
A=\lambda R(n-1),\quad
B=x(n),\quad
C=1,\quad
D=x^T(n)
$$

则：

$$
A^{-1}=\frac{1}{\lambda}P(n-1)
$$

代入引理并整理，得到：

$$
P(n)
=
\frac{1}{\lambda}
\left[
P(n-1)
-
\frac{
P(n-1)x(n)x^T(n)P(n-1)
}{
\lambda+x^T(n)P(n-1)x(n)
}
\right]
$$

定义增益向量：

$$
k(n)=
\frac{
P(n-1)x(n)
}{
\lambda+x^T(n)P(n-1)x(n)
}
$$

则协方差更新可写为：

$$
P(n)=
\frac{1}{\lambda}
\left[
P(n-1)-k(n)x^T(n)P(n-1)
\right]
$$

---

### 2.4 参数更新

先计算先验误差，也称新息：

$$
\alpha(n)=d(n)-x^T(n)w(n-1)
$$

然后更新滤波器系数：

$$
w(n)=w(n-1)+k(n)\alpha(n)
$$

---

### 2.5 算法流程

对每个时刻 $n=1,2,\dots$：
1. 计算先验误差：
$$
\alpha(n)=d(n)-x^T(n)w(n-1)
$$
2. 计算增益向量：
$$
k(n)=
\frac{
P(n-1)x(n)
}{
\lambda+x^T(n)P(n-1)x(n)
}
$$
3. 更新滤波器系数：
$$
w(n)=w(n-1)+k(n)\alpha(n)
$$
4. 更新协方差矩阵：
$$
P(n)=
\frac{1}{\lambda}
\left[
P(n-1)-k(n)x^T(n)P(n-1)
\right]
$$
5. 工程中可强制对称：
$$
P(n)\leftarrow \frac{P(n)+P^T(n)}{2}
$$
---

### 2.6 初始化

通常取：

$$
w(0)=0
$$

$$
P(0)=\delta I
$$

其中 $\delta$ 常取 $10^2\sim 10^6$。

- $\delta$ 大：初始不确定性大，初始增益大，收敛快，但可能震荡
- $\delta$ 小：初始更新慢，收敛平稳

---

### 2.7 具体计算例子（一维）

取最简单的一维参数估计。

#### 设定

- 遗忘因子：$\lambda=0.9$
- 初始参数：$w(0)=0$
- 初始协方差：$P(0)=1$
- 真实参数：$w=2$
- 数据：

| $n$ | $x(n)$ | $d(n)$ |
|------|---------|---------|
| 1    | 1       | 2       |
| 2    | 2       | 4       |
| 3    | 3       | 6       |

一维时，公式退化为标量：

$$
\alpha(n)=d(n)-x(n)w(n-1)
$$

$$
k(n)=\frac{P(n-1)x(n)}{\lambda+x^2(n)P(n-1)}
$$

$$
w(n)=w(n-1)+k(n)\alpha(n)
$$

$$
P(n)=\frac{1}{\lambda}\left[P(n-1)-k(n)x(n)P(n-1)\right]
$$

#### $n=1$

$$
\alpha(1)=2-1\times 0=2
$$

$$
k(1)=\frac{1\times 1}{0.9+1^2\times 1}
=\frac{1}{1.9}\approx 0.5263
$$

$$
w(1)=0+0.5263\times 2\approx 1.0526
$$

$$
P(1)=\frac{1}{0.9}\left[1-0.5263\times 1\times 1\right]
\approx 0.5263
$$

#### $n=2$

$$
\alpha(2)=4-2\times 1.0526\approx 1.8948
$$

$$
k(2)=\frac{0.5263\times 2}{0.9+2^2\times 0.5263}
\approx 0.3503
$$

$$
w(2)=1.0526+0.3503\times 1.8948\approx 1.7163
$$

$$
P(2)=\frac{1}{0.9}\left[0.5263-0.3503\times 2\times 0.5263\right]
\approx 0.1751
$$

#### $n=3$

$$
\alpha(3)=6-3\times 1.7163\approx 0.8511
$$

$$
k(3)=\frac{0.1751\times 3}{0.9+3^2\times 0.1751}
\approx 0.2122
$$

$$
w(3)=1.7163+0.2122\times 0.8511\approx 1.8969
$$

$$
P(3)=\frac{1}{0.9}\left[0.1751-0.2122\times 3\times 0.1751\right]
\approx 0.0707
$$

#### 结果对比

| $n$ | 估计值 $w(n)$ | 真实值 |
|------|----------------|--------|
| 0    | 0              | 2      |
| 1    | 1.0526         | 2      |
| 2    | 1.7163         | 2      |
| 3    | 1.8969         | 2      |

估计值逐渐逼近真实值 $2$，协方差 $P(n)$ 逐渐减小。

---

## 3. 注意事项

### 3.1 持续激励条件

输入向量 $x(n)$ 必须满足持续激励，否则 $R(n)$ 可能奇异，参数不可辨识，估计值可能发散。

### 3.2 遗忘因子 $\lambda$

- $\lambda=1$：所有历史数据等权，适合平稳系统，但跟踪时变参数能力弱
- $0<\lambda<1$：指数遗忘旧数据，适合非平稳/时变系统
- $\lambda$ 越小：跟踪越快，但噪声敏感，参数抖动大
- $\lambda$ 越大：平滑越好，但跟踪越慢
- 常用范围：$0.95\sim 0.999$
- 有效记忆长度约为：

$$
N_{\text{eff}}\approx \frac{1}{1-\lambda}
$$

例如 $\lambda=0.99$ 时，有效记忆约 100 个样本。

### 3.3 初值选择

$w(0)$ 和 $P(0)$ 会影响收敛速度。$P(0)=\delta I$ 中 $\delta$ 过大可能导致初始震荡，过小则初始收敛慢。

### 3.4 数值稳定性

直接实现 RLS 可能出现：

- $P(n)$ 失去对称性
- $P(n)$ 失去正定性
- 数值误差累积导致发散

工程中常用：

- 强制对称：$P\leftarrow(P+P^T)/2$
- 正则化
- QR-RLS
- UD 分解 RLS
- 平方根 RLS

### 3.5 计算复杂度

设滤波器长度为 $N$：

- 每次更新计算复杂度：$O(N^2)$
- 存储复杂度：$O(N^2)$

RLS 收敛快于 LMS，但计算量更大。

### 3.6 与 LMS、Kalman 的关系

- 与 LMS 相比：RLS 收敛更快、精度更高，但计算复杂
- 与 Kalman 滤波相比：RLS 可看作参数为常数时的 Kalman 滤波特例
- 遗忘因子 $\lambda$ 可理解为引入过程噪声，使算法具备跟踪时变参数的能力

---

## 4. 工程应用

RLS 常用于在线参数估计和自适应滤波，例如：

1. **自适应滤波**
   - 回声消除
   - 自适应噪声抵消
   - 线性预测

2. **通信系统**
   - 信道估计
   - 信道均衡
   - 接收机自适应处理

3. **系统辨识**
   - ARX、ARMAX 模型在线辨识
   - 机械、化工、电力系统参数监测

4. **自适应控制**
   - 自校正调节器
   - 模型参考自适应控制中的参数估计

5. **信号处理**
   - 时变 AR 模型
   - 谱估计
   - 传感器校准

6. **大模型增量微调中的路由选择**
   - 在持续学习/增量微调场景中，用 RLS 训练路由器，为每个任务选择独立的 LoRA 子空间。
   - 优势：免回放旧数据，理论零遗忘，适合大模型持续学习。
   - 典型方案：Any-SSR、RLSEdit、KRLS-Attn、ATS 等。

工程建议：

- 输入输出先归一化、去均值
- 时变快时选较小 $\lambda$
- 时变慢或平稳时选较大 $\lambda$
- 高精度场景使用 QR-RLS 或 UD-RLS
- 监控 $P(n)$，异常时重置

---

## 5. Python 代码示例

```python
import numpy as np

class RLS:
    def __init__(self, n, lam=0.99, delta=1e3):
        self.w = np.zeros((n, 1))
        self.P = delta * np.eye(n)
        self.lam = lam

    def update(self, x, d):
        x = np.asarray(x, dtype=float).reshape(-1, 1)
        d = float(np.asarray(d).item())

        e = d - (x.T @ self.w).item()
        den = self.lam + (x.T @ self.P @ x).item()
        k = (self.P @ x) / den

        self.w = self.w + k * e
        self.P = (self.P - k @ x.T @ self.P) / self.lam
        self.P = (self.P + self.P.T) / 2

        return self.w.ravel().copy(), e


if __name__ == "__main__":
    np.random.seed(0)

    true_w = np.array([1.5, -2.0, 0.5])
    rls = RLS(n=3, lam=0.995, delta=1000)

    w_hat = None
    for k in range(2000):
        x = np.random.randn(3)
        d = x @ true_w + 0.1 * np.random.randn()
        w_hat, e = rls.update(x, d)

    print("真实系数:", true_w)
    print("估计系数:", w_hat)
```

---

## 6. 核心公式速查

增益：

$$
k(n)=\frac{P(n-1)x(n)}
{\lambda+x^T(n)P(n-1)x(n)}
$$

参数更新：

$$
w(n)=w(n-1)+k(n)
\left[d(n)-x^T(n)w(n-1)\right]
$$

协方差更新：

$$
P(n)=\frac{1}{\lambda}
\left[
P(n-1)-k(n)x^T(n)P(n-1)
\right]
$$

初始化：

$$
w(0)=0,\quad P(0)=\delta I
$$

---

## 7. 总结

RLS 是一种在线递推最小二乘算法，用于自适应滤波和参数估计。

核心思想：

- 在每个时刻最小化加权误差平方和
- 用遗忘因子 $\lambda$ 对历史数据指数加权
- 通过增益向量 $k(n)$ 按新息修正滤波器系数
- 通过协方差矩阵 $P(n)$ 表示参数不确定性
- 递推更新，避免每次重新求矩阵逆

一句话：

**RLS = 在线最小化加权误差平方和 + 指数遗忘 + 递推矩阵逆 + 新息修正。**

---

## 8. 补充：RLS 在大模型增量微调中的应用

### 8.1 问题：灾难性遗忘

- **专业**：顺序微调多个任务时，新任务梯度覆盖旧任务最优参数，旧任务性能骤降。
- **通俗**：像狗熊掰棒子，掰一个丢一个；像多人共用笔记本，新内容擦掉旧内容。

### 8.2 思路：隔离 + RLS 路由

- **隔离**：每个任务独立 LoRA 子空间，互不干扰。
- **路由**：RLS 训练路由器，根据输入特征选择正确 LoRA。
- **RLS 优势**：递归更新，免回放旧数据；顺序训练 ≡ 联合训练，理论零遗忘。

### 8.3 典型方案：Any-SSR

- 底层冻结，提取共享特征。
- 上层每任务独立 LoRA。
- RLS 路由器：`score = f(x) @ W_router`，`argmax` 选 LoRA。
- 效果：路由准确率近 100%，旧任务保留近完美。

### 8.4 核心更新（极简）

```python
e = target - f.T @ W
k = P @ f / (lam + f.T @ P @ f)
W = W + k @ e
P = (P - k @ f.T @ P) / lam
P = (P + P.T) / 2
```

### 8.5 注意事项

- 不要随意 `inv`，用 `solve` / `lstsq` / Cholesky。
- `P` 强制对称，`λ` 取 0.99~1.0，加 jitter。
- 高维特征先降维，或用对角/低秩 RLS。
- 监控 `P` 条件数，异常时重置。

### 8.6 一句话

RLS 在增量微调中做免回放路由器：任务子空间隔离 + 顺序学习不遗忘。

---

## 9. 大模型例子 Python 代码

  
- 冻结特征提取器（模拟大模型底层）  
- 每个任务一个独立线性头（模拟 LoRA）  
- RLS 路由器增量学习任务选择  
- 顺序训练多个任务，不访问旧数据  

```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# ============================================================
# 1. 冻结特征提取器（模拟大模型底层）
# ============================================================
class FrozenBackbone(nn.Module):
    def __init__(self, in_dim=20, feat_dim=32):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, 64),
            nn.ReLU(),
            nn.Linear(64, feat_dim)
        )
        for p in self.parameters():
            p.requires_grad = False

    def forward(self, x):
        return self.net(x)

# ============================================================
# 2. 每个任务的独立头（模拟 LoRA）
# ============================================================
class TaskHead(nn.Module):
    def __init__(self, feat_dim, out_dim=1):
        super().__init__()
        self.fc = nn.Linear(feat_dim, out_dim)

    def forward(self, f):
        return self.fc(f)

# ============================================================
# 3. RLS 路由器
# ============================================================
class RLSRouter:
    def __init__(self, feat_dim, n_tasks, lam=1.0, delta=1e3):
        self.W = np.zeros((feat_dim, n_tasks))
        self.P = delta * np.eye(feat_dim)
        self.lam = lam

    def update(self, f, target):
        f = f.reshape(-1, 1)             # f:列向量
        target = target.reshape(1, -1)   # target:行向量
        den = self.lam + float(f.T @ self.P @ f) #标量
        k = (self.P @ f) / den                   #列向量
        pred = f.T @ self.W                      #行向量
        self.W = self.W + k @ (target - pred)    # 外积更新
        self.P = (self.P - k @ f.T @ self.P) / self.lam  #更新相关矩阵
        self.P = (self.P + self.P.T) / 2  #强制对称

    def predict(self, f):
        return np.argmax(f @ self.W, axis=-1)

# ============================================================
# 4. 生成任务数据
# ============================================================
def generate_task_data(n_tasks, n_samples, in_dim=20):
    tasks = []
    for k in range(n_tasks):
        X = torch.randn(n_samples, in_dim)
        true_w = torch.randn(in_dim, 1) * (k + 1)
        y = X @ true_w + 0.1 * torch.randn(n_samples, 1)
        tasks.append((X, y))
    return tasks

# ============================================================
# 5. 顺序增量训练
# ============================================================
def main():
    torch.manual_seed(0)
    np.random.seed(0)

    in_dim = 20
    feat_dim = 32
    n_tasks = 3
    n_samples_per_task = 200

    backbone = FrozenBackbone(in_dim, feat_dim)
    task_heads = [TaskHead(feat_dim) for _ in range(n_tasks)]
    router = RLSRouter(feat_dim, n_tasks, lam=1.0, delta=1e3)

    tasks = generate_task_data(n_tasks, n_samples_per_task, in_dim)

    for k, (X, y) in enumerate(tasks):
        head = task_heads[k]
        optimizer = optim.Adam(head.parameters(), lr=1e-2)
        loss_fn = nn.MSELoss()

        for epoch in range(100):
            optimizer.zero_grad()
            F = backbone(X)
            pred = head(F)
            loss = loss_fn(pred, y)
            loss.backward()
            optimizer.step()

        with torch.no_grad():
            F = backbone(X).numpy()
            for i in range(len(X)):
                target = np.zeros(n_tasks)
                target[k] = 1.0
                router.update(F[i], target)

        print(f"任务 {k} 完成，最终 loss={loss.item():.4f}")

    print("\n=== 测试结果 ===")
    total_mse = 0.0
    total_n = 0

    for k, (X, y) in enumerate(tasks):
        with torch.no_grad():
            F = backbone(X).numpy()
            pred_task = router.predict(F)
            acc = np.mean(pred_task == k)

            F_tensor = torch.tensor(F, dtype=torch.float32)
            y_pred = task_heads[k](F_tensor).numpy()
            mse = np.mean((y.numpy() - y_pred) ** 2)

            print(f"任务 {k}: 路由准确率={acc:.2%}, MSE={mse:.4f}")

            total_mse += np.sum((y.numpy() - y_pred) ** 2)
            total_n += len(y)

    print(f"整体 MSE: {total_mse / total_n:.4f}")

if __name__ == "__main__":
    main()
```

**说明**：  
- 这是一个极简模拟，真实大模型只需把 `FrozenBackbone` 换成冻结的 Transformer 底层，把 `TaskHead` 换成 LoRA 模块。  
- RLS 路由器只更新自身参数，不更新大模型权重。  
- 顺序训练时，路由器通过 RLS 递归更新，不访问旧任务数据，从而实现免回放的任务选择。

---

## 附录：矩阵求逆引理 $(A+BCD)^{-1}$ 的分块矩阵证明

### 引理

设 $A\in\mathbb{R}^{n\times n}$，$C\in\mathbb{R}^{m\times m}$ 可逆，$B\in\mathbb{R}^{n\times m}$，$D\in\mathbb{R}^{m\times n}$，且 $A+BCD$ 与 $C^{-1}+DA^{-1}B$ 可逆，则：

$$
(A+BCD)^{-1}
=
A^{-1}
-
A^{-1}B
\left(C^{-1}+DA^{-1}B\right)^{-1}
DA^{-1}
$$

### 分块矩阵证明

构造分块矩阵：

$$
M=
\begin{bmatrix}
A & B\\
-D & C^{-1}
\end{bmatrix}
$$

#### 第一种消元方式

左乘：

$$
\begin{bmatrix}
I & 0\\
DA^{-1} & I
\end{bmatrix}
$$

得到：

$$
\begin{bmatrix}
A & B\\
0 & C^{-1}+DA^{-1}B
\end{bmatrix}
$$

令：

$$
S=C^{-1}+DA^{-1}B
$$

则 $M^{-1}$ 的 $(1,1)$ 块为：

$$
A^{-1}-A^{-1}BS^{-1}DA^{-1}
$$

#### 第二种消元方式

左乘：

$$
L=
\begin{bmatrix}
I & -BC\\
0 & I
\end{bmatrix}
$$

则：

$$
LM=
\begin{bmatrix}
A+BCD & 0\\
-D & C^{-1}
\end{bmatrix}
$$

其逆矩阵的 $(1,1)$ 块为：

$$
(A+BCD)^{-1}
$$

因此：

$$
(A+BCD)^{-1}
=
A^{-1}
-
A^{-1}B
\left(C^{-1}+DA^{-1}B\right)^{-1}
DA^{-1}
$$

证毕。

### 在 RLS 中的应用

取：

$$
A=\lambda R(n-1),\quad
B=x(n),\quad
C=1,\quad
D=x^T(n)
$$

则：

$$
A^{-1}=\frac{1}{\lambda}P(n-1)
$$

代入引理即可得到 RLS 的协方差矩阵递推公式：

$$
P(n)
=
\frac{1}{\lambda}
\left[
P(n-1)
-
\frac{
P(n-1)x(n)x^T(n)P(n-1)
}{
\lambda+x^T(n)P(n-1)x(n)
}
\right]
$$