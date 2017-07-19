# -*- coding: utf-8 -*-
"""
Created by hushiwei on 16-12-22.
"""
'''
python 装饰器用法
'''
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print 'call %s():' % (func.__name__)
        return func(*args,**kw)
    return wrapper

def logg(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kv):
            print '%s %s():' %(text,func.__name__)
            return func(*args,**kv)
        return wrapper
    return decorator

@logg('dec')
def now():
    print "hello world"

now()
print now.__name__
