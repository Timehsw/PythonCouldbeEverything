#coding:utf-8
'''
    Created on 2016/5/31 0031 
    @Author:   HuShiwei
'''

import os
from PIL import Image

fs=open("C:\jusfoun\\likehua.txt",'r')
print fs.read()

fs.close()

# print os.name
print os.environ
print os.getenv("path")

print os.path.abspath(".")
print "========================================="

im=Image.open('C:\jusfoun\\lufei.jpg')
w,h=im.size
print w,h


