# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/25.
'''

import threading


def fun():
    print 'hello world'

def fun1(num):
    for i in range(num):
        print 'count %d' % i


t1=threading.Thread(target=fun())
t1.start()

t2=threading.Thread(target=fun1,args=(5,))
t2.start()

