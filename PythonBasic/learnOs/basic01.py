# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/3/19
"""

'''
1.获取当前脚本路径
2.获取当前路径
3.改变目录
'''
import os

print os.getcwd()
print os.getenv("SCALA_HOME")

path = '/Users/hushiwei/IdeaProjects/PythonCouldbeEverything'
files = os.listdir(path)
print os.path.isdir(path)
print "----------------"

for file in files:
    if os.path.isdir(os.path.join(path, file)):
        print "dir: ", file
    else:
        print "file: ", file

print "----------------"

# ss=os.system('ls ')
# print ss
#
# print os.sep
# print os.linesep
# print "----------------"
# print os.path.split(path)
# print os.path.dirname(path)
# print os.path.basename(path)
# print '~'*60
# print os.path.dirname(__file__)
# print os.getcwd()
# # 获取当前脚本的路径
# print os.path.abspath(__file__)
# print os.path.abspath('')
# # 获取当前脚本所在的目录路径
print os.path.dirname(os.path.abspath(__file__))
# # 获取脚本名字
print os.path.basename(os.path.abspath(__file__))
print os.getcwd()
os.chdir(path)
print os.getcwd()
