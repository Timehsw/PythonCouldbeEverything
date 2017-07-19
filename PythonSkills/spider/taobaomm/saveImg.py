#coding:utf-8
'''
    Created on 2016/8/22 0022 
    @Author:   HuShiwei
'''

import urllib

url='http://img.xxdm.org/allimg/131118/5_131118111740_1.jpg'

def saveImg(url):
    data=urllib.urlopen(url)
    img=data.read()

    file=open('imgPac.jpg','wb')
    file.write(img)
    print "保存图片完成"
    file.close()

saveImg(url)