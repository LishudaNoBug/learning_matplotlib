import matplotlib.pyplot as plt
import numpy as np
"""
    基本的直线图
    
    关于plot的参数：https://www.jianshu.com/p/ed3f31fc6a41
    'b' 蓝色 'm' 洋红色 magenta
    'g' 绿色 'y' 黄色
    'r' 红色 'k' 黑色
    'w' 白色 'c' 青绿色 cyan
    '#008000' RGB某颜色 '0.8' 灰度值字符串
    多条曲线不指定颜色时，会自动选择不同颜色
    风格字符
    '‐' 实线
    '‐‐' 破折线
    '‐.' 点划线
    ':' 虚线
    '' ' ' 无线条

"""

x = np.linspace(-1, 1, 50)
y = 2*x + 1
# y = x**2
plt.plot(x, y)
plt.show()