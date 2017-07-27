# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/27.
'''

'''
一维数组相关操作
'''
import numpy as np

a = [1, 2, 3, 4]
# 将python的列表构造成numpy中的ndarray类型了
b=np.array(a)
print type(b)

# 返回最大值的位置也就是3
print b.argmax()
# 求最大值也就是4
print b.max()
# 求平均数也就是2.5
print b.mean()
