import matplotlib.pyplot as plt
import numpy as np

""" 将窗口调成 x、y轴的坐标系形状
    ax = plt.gca()      # 获取当前的所有轴
    ax.spines['right'].set_color('none') # （将右边和上面的轴去掉）
    ax.spines['top'].set_color('none')
"""

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

# 在一个窗口内画出y2、y1两条线，设置窗口内x坐标范围-1~2，y坐标范围-2~3
plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# 调整x、y的显示（对于我以后来说应该用不上）
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],['$really\ bad$', '$bad$', '$normal$', '$good$', '$really\ good$'])

# 将左边和上边的边框去掉
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 将底下的边框设置为x轴，让他相交于y轴的data数据 0位置
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
# 将左边的边框设置为y轴，让他相交于x轴的data数据 0位置
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plt.show()