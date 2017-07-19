# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/3/18
"""
import shutil
'''
shutil 是高级的文件，文件夹，压缩包处理模块。
'''

'''
1.
shutil.copyfileobj(fsrc, fdst[, length])
将文件内容拷贝到另一个文件中
'''

shutil.copyfileobj(open('old.xml','r'), open('new.xml', 'w'))