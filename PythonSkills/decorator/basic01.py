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
无参装饰器
'''


def a_new_decorator(a_func):
    def wrapTheFunction():
        print "I am doing some boring work before execution a_func()"
        a_func()
        print "I am doing some boring work after  execution a_func()"

    return wrapTheFunction


def a_function_requiring_decoration():
    print "I am the function which needs some decoration to remove my foul smell"


# 单独的调用这个函数,原样输出
a_function_requiring_decoration()

# 将这个函数的引用传入另一个函数,并把返回的函数引用也命名为之前的函数
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

# 现在再次调用这个函数,实际上引用的是wrapTheFunction这个被包装了的函数
a_function_requiring_decoration()

print '~'*80
###################################################################################

# 现在让我们用@符号来写装饰器

###################################################################################

@a_new_decorator
def a_function_have_decoration():
    print "I am the function which have some decoration to remove my foul smell"


'''
@修饰后,自动的做了这些事情
1.将@a_new_decorator下一行的函数名称作为参数传给a_new_decorator函数
2.将返回的函数名称指向a_function_have_decoration
3.但是实际上此时a_function_have_decoration是wrapTheFunction这个函数
4.所以这样就起到了装饰的作用
'''
print a_function_have_decoration.__name__  #wrapTheFunction
a_function_have_decoration()
