# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/8/31.
'''

'''
哈希算法,均匀分散数据

'''

from hashlib import md5
from struct import unpack_from

# 1千万个数
TIMES=10000000

# 100个节点
NODES=100

node_stat=[0 for i in range(NODES)]


for item in range(TIMES):
    k=md5(str(item)).digest()
    h=unpack_from(">I",k)[0]
    n=h % NODES
    node_stat[n]+=1

print node_stat

_ave = TIMES / NODES
_max = max(node_stat)
_min = min(node_stat)

print("Ave: %d" % _ave)
print("Max: %d\t(%0.2f%%)" % (_max, (_max - _ave) * 100.0 / _ave))
print("Min: %d\t(%0.2f%%)" % (_min, (_ave - _min) * 100.0 / _ave))
