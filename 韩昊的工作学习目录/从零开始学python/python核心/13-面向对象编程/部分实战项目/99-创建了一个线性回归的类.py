"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

# =========================
# 1. 生成模拟数据
# =========================
n = 300

area = np.random.normal(120, 35, n)          # 面积
bedrooms = np.random.randint(1, 6, n)        # 卧室数
age = np.random.randint(0, 30, n)            # 房龄
noise = np.random.normal(0, 20, n)           # 噪声

# 真实关系：price = 50 + 0.9 * area + 8 * bedrooms - 1.5 * age + noise
price = 50 + 0.9 * area + 8 * bedrooms - 1.5 * age + noise

X = np.column_stack([area, bedrooms, age])
y = price

df = pd.DataFrame(X, columns=["area", "bedrooms", "age"])
df["price"] = y

print("数据预览：")
print(df.head())
print("\n数据统计：")
print(df.describe())

# =========================
# 2. 手动划分训练集和测试集
# =========================
indices = np.random.permutation(n)
split = int(0.8 * n)

train_idx = indices[:split]
test_idx = indices[split:]

X_train_raw = X[train_idx]
X_test_raw = X[test_idx]
y_train = y[train_idx]
y_test = y[test_idx]

# =========================
# 3. 手动标准化
# 注意：只能用训练集均值方差
# =========================
mu = X_train_raw.mean(axis=0)
sigma = X_train_raw.std(axis=0)

X_train = (X_train_raw - mu) / sigma
X_test = (X_test_raw - mu) / sigma

# =========================
# 4. 从零实现线性回归
# =========================
class LinearRegressionScratch:
    def __init__(self, method="gd", learning_rate=0.05, n_iters=5000, reg_lambda=0.0):
        """
        method: "gd" 梯度下降, "normal" 正规方程
        learning_rate: 学习率
        n_iters: 梯度下降迭代次数
        reg_lambda: L2 正则化系数
        """
        self.method = method
        self.learning_rate = learning_rate
        self.n_iters = n_iters
        self.reg_lambda = reg_lambda
        self.theta = None
        self.loss_history = []

    def _add_bias(self, X):
        """添加偏置列，即全 1 列"""
        return np.c_[np.ones((X.shape[0], 1)), X]

    def _loss(self, X_b, y):
        """计算损失，用于记录"""
        m = len(y)
        err = X_b @ self.theta - y
        loss = (err @ err) / (2 * m)

        if self.reg_lambda > 0:
            loss += (self.reg_lambda / (2 * m)) * np.sum(self.theta[1:] ** 2)

        return loss

    def fit(self, X, y):
        X_b = self._add_bias(X)
        m, n_features = X_b.shape

        self.theta = np.zeros(n_features)
        self.loss_history = []

        if self.method == "normal":
            # 正规方程解
            # 如果 reg_lambda > 0，则是岭回归
            I = np.eye(n_features)
            I[0, 0] = 0  # 不正则化截距

            self.theta = (
                np.linalg.pinv(X_b.T @ X_b + self.reg_lambda * I)
                @ X_b.T
                @ y
            )
            self.loss_history.append(self._loss(X_b, y))

        elif self.method == "gd":
            # 梯度下降
            for i in range(self.n_iters):
                err = X_b @ self.theta - y
                grad = (X_b.T @ err) / m

                # L2 正则，不正则化截距
                if self.reg_lambda > 0:
                    grad[1:] += (self.reg_lambda / m) * self.theta[1:]

                self.theta -= self.learning_rate * grad

                if i % 100 == 0:
                    self.loss_history.append(self._loss(X_b, y))

            self.loss_history.append(self._loss(X_b, y))

        else:
            raise ValueError("method 必须是 'gd' 或 'normal'")

        return self

    def predict(self, X):
        X_b = self._add_bias(X)
        return X_b @ self.theta

    def score(self, X, y):
        """R²"""
        y_pred = self.predict(X)
        sse = np.sum((y - y_pred) ** 2)
        sst = np.sum((y - np.mean(y)) ** 2)
        return 1 - sse / sst


# =========================
# 5. 评估指标
# =========================
def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def rmse(y_true, y_pred):
    return np.sqrt(mse(y_true, y_pred))

def mae(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))

def r2_score(y_true, y_pred):
    sse = np.sum((y_true - y_pred) ** 2)
    sst = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - sse / sst


# =========================
# 6. 训练模型
# =========================
gd_model = LinearRegressionScratch(
    method="gd",
    learning_rate=0.05,
    n_iters=5000,
    reg_lambda=0.0
)
gd_model.fit(X_train, y_train)

normal_model = LinearRegressionScratch(
    method="normal",
    reg_lambda=0.0
)
normal_model.fit(X_train, y_train)


# =========================
# 7. 将标准化空间的参数转回原始尺度
# y = theta0 + theta1 * x1_scaled + ...
# x_scaled = (x - mu) / sigma
# =========================
def to_original_scale(theta, mu, sigma):
    b = theta[0] - np.sum(theta[1:] * mu / sigma)
    w = theta[1:] / sigma
    return b, w


# =========================
# 8. 评估
# =========================
print("\n================ 梯度下降模型 ================")
y_pred_gd = gd_model.predict(X_test)
print("标准化空间 theta：", gd_model.theta)
print("MSE :", mse(y_test, y_pred_gd))
print("RMSE:", rmse(y_test, y_pred_gd))
print("MAE :", mae(y_test, y_pred_gd))
print("R²  :", r2_score(y_test, y_pred_gd))

b_gd, w_gd = to_original_scale(gd_model.theta, mu, sigma)
print("原始尺度截距：", b_gd)
print("原始尺度系数 [area, bedrooms, age]：", w_gd)

print("\n================ 正规方程模型 ================")
y_pred_normal = normal_model.predict(X_test)
print("标准化空间 theta：", normal_model.theta)
print("MSE :", mse(y_test, y_pred_normal))
print("RMSE:", rmse(y_test, y_pred_normal))
print("MAE :", mae(y_test, y_pred_normal))
print("R²  :", r2_score(y_test, y_pred_normal))

b_normal, w_normal = to_original_scale(normal_model.theta, mu, sigma)
print("原始尺度截距：", b_normal)
print("原始尺度系数 [area, bedrooms, age]：", w_normal)

print("\n真实生成关系：")
print("price = 50 + 0.9 * area + 8 * bedrooms - 1.5 * age + noise")
print("所以理想系数约为：[0.9, 8, -1.5]，截距约为 50")


# =========================
# 9. 可视化
# =========================
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 损失曲线
axes[0].plot(gd_model.loss_history)
axes[0].set_title("Gradient Descent Loss Curve")
axes[0].set_xlabel("Iteration (recorded every 100)")
axes[0].set_ylabel("Loss")

# 梯度下降预测效果
axes[1].scatter(y_test, y_pred_gd, alpha=0.6)
axes[1].plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    "r--"
)
axes[1].set_title("GD: True vs Predicted")
axes[1].set_xlabel("True Price")
axes[1].set_ylabel("Predicted Price")

# 正规方程预测效果
axes[2].scatter(y_test, y_pred_normal, alpha=0.6)
axes[2].plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    "r--"
)
axes[2].set_title("Normal Equation: True vs Predicted")
axes[2].set_xlabel("True Price")
axes[2].set_ylabel("Predicted Price")

plt.tight_layout()
plt.show()
#