import matplotlib.pyplot as plt
import numpy as np


""" 设置x、y轴坐标刻度范围:

    plt.xlim((-1, 2))   设置x轴坐标范围（x limit ，只显示指定范围内数据，超过边框的数据就显示不全）
    plt.ylim((-2, 3))   设置y轴坐标范围

    plt.xlabel('I am x')    x轴取别名
    plt.ylabel('I am y')    y轴取别名
    
    new_ticks = np.linspace(-1, 2, 5)   x坐标轴刻度重新替换自己的刻度
    print(new_ticks)
    plt.xticks(new_ticks)
    
    plt.yticks([-2, -1.8, -1, 1.22, 3],[r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$']) y坐标轴刻度替换为自己的刻度（文字）
"""



x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('I am x')
plt.ylabel('I am y')


new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],[r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
plt.show()