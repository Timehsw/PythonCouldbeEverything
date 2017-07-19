# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/3/29
"""

import os
filepath=os.path.join(os.path.dirname(os.getcwd()),"area.properties")
'''
1、read( )：表示读取全部内容
2、readline( )：表示逐行读取
3.循环读取每一行
'''
file=open(filepath,'r+')
print file.readline()
# for line in file:
#     print line