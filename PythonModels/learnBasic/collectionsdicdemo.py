# -*- coding: utf-8 -*-
"""
Created by hushiwei on 17-1-10.
"""

from collections import OrderedDict

# d={'t':'a','r':'d','y':'f'}
f=[('t','a'),('r','d'),('y','f')]


# OrderedDict的key是有顺序的
d2=OrderedDict([('t','a'),('r','d'),('y','f')])
print d2
d3=d2.popitem()[1]
print d3
# d2=OrderedDict()
# print d2

# for k,v in f:
#     print k,v

# while d2:
#     yield d2.popitem(last=False)[1]