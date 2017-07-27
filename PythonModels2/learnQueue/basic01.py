# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/25.
'''

'''
队列数据结构
'''
import Queue

# 构造一个队列,最大放10个元素
myqueue=Queue.Queue(maxsize=10)

# 往队列中放入数据
for i in range(1,11):
    myqueue.put(i)

# 从队列中取数
for i in range(10):
    print myqueue.get()
