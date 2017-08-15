# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/8/10.
'''


with open('./tables.txt','r') as f:
    lines=f.readlines(10000)
    for line in lines:
        print "--->"+line