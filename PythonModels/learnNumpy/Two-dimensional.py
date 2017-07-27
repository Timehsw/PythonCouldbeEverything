# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/27.
'''
'''
二维数组相关操作
'''
import numpy as np

a=[[1,2],[3,4]]
b=np.array(a)

print b

print b.shape
print b.size
print b.max(axis=0)
print b.max(axis=1)
print b.mean(axis=0)

print b.flatten()

print b.ravel()
