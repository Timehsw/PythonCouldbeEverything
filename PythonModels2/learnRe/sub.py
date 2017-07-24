# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/7/20
"""

'''
正则替换功能
'''

import re

pattren=re.compile(r"(\w+) (\w+)")

str="hello 123, hello 456"

# 把str中匹配到的替换成hello world
m=pattren.sub("hello world",str)

print m


# demo2

