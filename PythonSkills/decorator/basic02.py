# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2018/1/7.
    学习装饰器
    闭包
    函数里面可以定义函数
    函数可以被传递赋值
    函数可以被返回

    那么装饰器就是,在函数之前额外做些事情
'''

'''
装饰器
有参函数
'''


def a_new_decorator(a_func):
    def wrapTheFunction(*args,**kwargs):
        print "I am doing some boring work before execution a_func()"
        a_func(*args,**kwargs)
        print "I am doing some boring work after  execution a_func()"

    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration(name="hushiwei"):
    print "I am %s"%name


a_function_requiring_decoration("Mike")


