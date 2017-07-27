# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/27.
'''

'''
matplotlib绘制2D图表 点和线
^(.*):\s(.*):\s(.*):\s(.*)$
'''
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 通过rcParams设置全局横纵轴字体大小
mpl.rcParams['xtick.labelsize']=24
mpl.rcParams['ytick.labelsize']=24

# x轴的点
x1 = np.arange(11)
# y轴的点
y1 = [
    1.0847275042134147E-4,
    2.0106877828356476E-4,
    1.1836360644802181E-4,
    0.043453404423487926,
    0.03113001646083574,
    0.06,
    0.012709253496067191,
    0.06,
    3.284899860591644E-4,
    0.015235253124714847,
    0.0034946847451197242,
]

# 创建一个图,名字为ctr
# plt.figure("ctr")
# 在图上绘制
# plt.plot(x1,y1)


x2 = np.arange(11)

y2 = [
    3.529088519807792E-5,
    1.1895968858318187E-4,
    0.0013049292594645469,
    0.046417845349992326,
    0.03282177644291713,
    0.06,
    0.013313023920004725,
    0.06,
    3.554547063283854E-4,
    0.014309633417956262,
    0.0034946847451197242,
]


# plt.figure("ctrEstimate")
# plt.plot(x2,y2,'k')


# 两个图画一起
plt.figure('ctr & ctrEstimate')
plt.plot(x1, y1)

# scatter可以方便出散点图
# plt.scatter(x1,y11,c='red',marker='v')

# plt.scatter(x2,y22,marker='^')

# 'r'表示用红色线
plt.plot(x2, y2, 'r')
plt.savefig("ctr2.png")

plt.show()
