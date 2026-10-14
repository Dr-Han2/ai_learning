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
from matplotlib.colors import ListedColormap
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier,plot_tree


def load_datafromexcel(path):
    Sample_excel =pd.read_csv(path,header= 0, index_col = 0)
    Sample = Sample_excel.values
    y= Sample[:,Sample.shape[1]-1]
    print(y)
    X= Sample[:,0:Sample.shape[1]-1]
    print(X)
    return X,y

def draw_figure(X,y,clf):
    h = .02
    cmap_light = ListedColormap(['orange','cyan','cornflowerblue'])
    cmap_bold = ListedColormap(['darkorange','c','darkblue'])
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy =np.meshgrid(np.arange(x_min, x_max, h),np.arange(y_min, y_max, h))
    y_predict =clf.predict(np.c_[xx.ravel(), yy.ravel()])
    y_predict = y_predict.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, y_predict, cmap = cmap_light)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap = cmap_bold,edgecolors='k',s=20)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("Iris 2 feature 2 laabel")
    return

if __name__ == '__main__':
    X_train, y_train = load_datafromexcel(path = 'iris_2feature2label_train.csv')
    X_train = X_train[:,:2]
    X_test , y_test = load_datafromexcel(path = 'iris_2feature2label_test.csv')
    X_test = X_test[:,:2]

    clf =DecisionTreeClassifier(max_depth= 2)
    clf.fit(X_train, y_train)
    y_predict_train =clf.predict(X_train)
    print(classification_report(y_train,y_predict_train))

    y_predict_test =clf.predict(X_test)
    print(classification_report(y_test,y_predict_test))

    draw_figure(X_train,y_train,clf)
    plt.figure(2)
    plot_tree(clf, filled=True)
    plt.figure(3)
    draw_figure(X_train,y_train,clf)
    plt.show()

