"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# 1. 加载原始 Iris 数据集
iris = load_iris()
X = iris.data
y = iris.target

# 2. 筛选：只取前两个特征 (0, 1)，只取前两个类别 (0, 1)
# 原始数据里类别 0 和 1 是线性可分的
mask = y < 2
X = X[mask][:, :2]
y = y[mask]

# 3. 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 4. 拼回 DataFrame 并保存为 CSV
# 你的 load_data 函数第一列会当作 index_col，所以第一列放个索引
train_df = pd.DataFrame(X_train, columns=['feat1', 'feat2'])
train_df['label'] = y_train
train_df.to_csv('iris_2feature2label_train.csv')

test_df = pd.DataFrame(X_test, columns=['feat1', 'feat2'])
test_df['label'] = y_test
test_df.to_csv('iris_2feature2label_test.csv')

print("CSV 文件已生成！")