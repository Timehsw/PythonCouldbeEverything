#coding:utf-8
'''
    Created on 2016/5/31 0031 
    @Author:   HuShiwei
'''
import logging
logging.basicConfig(level=logging.INFO)
def func(x):
    a=int(x)
    assert a!=0,"a is zero"
    print a

func(10)

s='0'
n=int(s)
logging.info('n=%d' %n)
print 10/n

