# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/3/29
"""

import os

path=os.getcwd()
'''
#返回文件目录或者路径的父目录
split[0] ===> os.path.dirname
#返回目录或者文件名
split[1] ===> os.path.basename
'''
print os.path.split(__file__)[0]
print os.path.split(__file__)[1]

print os.path.split(path)[0]
print os.path.split(path)[1]

print os.path.dirname(__file__)
print os.path.basename(__file__)

'''
#判断文件、目录是否存在
#os.path.isfile判断是否为文件 os.path.isdir判断是否为目录
'''
print os.path.exists(path)

'''
#拼接路径， 以系统分隔符 (os.sep)
'''
filename='area.properties'
confpath=os.path.join(os.path.dirname(path),filename)
if os.path.exists(confpath):
    print confpath