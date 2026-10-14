"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. 加载数据
iris = load_iris()
X, y = iris.data, iris.target

# 2. 划分数据集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# 3. 训练决策树
dt = DecisionTreeClassifier(
    criterion='gini',      # 分裂标准：'gini' 或 'entropy'
    max_depth=3,           # 最大深度（防止过拟合）
    random_state=42
)
dt.fit(X_train, y_train)
tu

# 4. 评估
y_pred = dt.predict(X_test)
print("训练集准确率:", dt.score(X_train, y_train))
print("测试集准确率:", accuracy_score(y_test, y_pred))
print("\n混淆矩阵:\n", confusion_matrix(y_test, y_pred))
print("\n分类报告:\n", classification_report(y_test, y_pred, target_names=iris.target_names))
