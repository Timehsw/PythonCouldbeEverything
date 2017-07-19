# coding:utf-8
'''
    Created on 2016/8/20 0020 
    @Author:   HuShiwei
'''

import urllib2
import urllib
import re
import os

class MeiMei:
    def __init__(self):
        self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'

    def getPage(self, pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        print "第%d页地址:%s" %(pageIndex,url)
        resquest=urllib2.Request(url)
        response=urllib2.urlopen(resquest)
        return response.read().decode('gbk')

    def getContent(self,pageIndex):
        page=self.getPage(pageIndex)
        pattern=re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        items=re.findall(pattern,page)
        for item in items:
            print item[0],item[1],item[2],item[3],item[4]

#     写入图片,传入图片地址,文件名,保存单张图片
    def saveImg(self,imageUrl,filename):
        u=urllib.urlopen(imageUrl)
        data=u.read()
        f=open(filename,'wb')
        f.write(data)
        f.close()
#     写入文本
    def saveBrief(self,content,name):
        fileName=name+"/"+name+".txt"
        f=open(fileName,"w+")
        print u"正在保存她的个人信息为",fileName
        f.write(content.encode('utf-8'))
#     创建新目录
    def mkdir(self,path):
        path=path.strip()
#         判断路径是否存在,存在true,不存在false
        isExists=os.path.exists(path)
        if not isExists:
            os.mkdir(path)
            return True
        else:
            return False

spider=MeiMei()
spider.getContent(1)

