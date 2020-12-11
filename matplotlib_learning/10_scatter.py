import matplotlib.pyplot as plt
import numpy as np

""" 散点图
    plt.scatter(X, Y, s=75, c=T, alpha=.5)      # X，Y就是点的xy数据集合，s是size大小；c是color颜色；alpha是透明度。 
"""

n = 1024    # data size
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)    # for color later on

plt.scatter(X, Y, s=75, c=T, alpha=.5)

plt.xlim(-1.5, 1.5)
plt.xticks(())  # 隐藏掉刻度值
plt.ylim(-1.5, 1.5)
plt.yticks(())  # 隐藏掉刻度值

plt.show()