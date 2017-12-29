# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/12/28.
'''



def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper


@log
def now():
    print '2013-12-25'


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator



if __name__ == '__main__':
    now()