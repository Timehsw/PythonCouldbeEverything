# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/22.
'''
'''
获取知乎收藏夹图片小爬虫
爬虫正常运行需要获取登录后的cookie值
'''

import requests
from lxml import html
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class Zhihu:
    def __init__(self):
        self.baseCollectUrl = 'https://www.zhihu.com/collection/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
            "Cookie": 'd_c0="ACCCItg0bguPTuSWzkKoBlPEFSv_VHbV4f4=|1489154388"; _zap=a1cd94b2-4f86-4883-917b-3915b8cb26e9; _ga=GA1.2.1981484424.1494568992; r_cap_id="NzQxYTE5MGNiNTE4NDk5Mjg4M2FjZTJjMGE1ZjM2NTc=|1498541307|3757c40a1662d8408b6edf67f352361bb24a81e2"; cap_id="MGI3ZDQwOWI4ZWY2NGZkNDkyZDVmMDdiZDk3ZmI5NWM=|1498541307|4bcc436cdfa7cbddf850f22cbf2a0813d527dbc7"; z_c0=Mi4wQUFDQWViRWNBQUFBSUlJaTJEUnVDeGNBQUFCaEFsVk5fbmw1V1FEeEFKcU9fV05IT3hXbk1oU05xVXdqazFKZk9B|1498541310|abb3f10588b5aaf8629f9c3b908fc96ee07010a2; q_c1=2343456a6f4546169eff16afd3ca3eda|1500188880000|1489154388000; q_c1=2343456a6f4546169eff16afd3ca3eda|1500188880000|1489154388000; aliyungf_tc=AQAAAPpv11DjqwEAAS10e/kIN5mMraiF; _xsrf=21251e64-0e14-487d-ade9-ec26e3b48d7c; __utma=51854390.1981484424.1494568992.1500603028.1500734369.2; __utmb=51854390.0.10.1500734369; __utmc=51854390; __utmz=51854390.1500734369.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100-1|2=registration_date=20130729=1^3=entry_date=20130729=1'
        }

    def fromCollectionFindAnswer(self, collection, pageNum):
        '''
        从收藏中找到各个回答的链接
        :param collection:
        :param pageNum:
        :return:
        '''
        collection_title = None
        url = self.baseCollectUrl + "{}?page={}".format(collection, pageNum)
        print url
        response = requests.get(url, headers=self.headers).content
        content = html.fromstring(response)
        # 以收藏夹名字创建文件夹
        if collection_title is None:
            collection_title = content.xpath('//h2[@class="zm-item-title zm-editable-content"]/text()')[0].strip()
            print collection_title
            if not os.path.exists(collection_title):
                os.mkdir(collection_title)

        answerLinks = content.xpath('//div[@class="zm-item"]//a[@class="toggle-expand"]/@href')
        for link in answerLinks:
            answerFullLinks = "https://www.zhihu.com{}".format(link)
            self.fromAnswerGetPicLinks(collection_title, answerFullLinks)

    def fromAnswerGetPicLinks(self, collection_title, answerFullLinks):
        '''
        从回答里面获取所有的图片链接
        :param collection_title:
        :param answerFullLinks:
        :return:
        '''
        response = requests.get(answerFullLinks, headers=self.headers).content
        content = html.fromstring(response)
        #         获取问题名称,获取回答人名字拼成文件夹名字
        # 获取问题名称
        title = content.xpath('//h1[@class="QuestionHeader-title"]/text()')[0].strip()
        try:
            author = content.xpath('//div[@class="AuthorInfo-head"]//a[@class="UserLink-link"]/text()')[0].strip()
        except:
            author = u'匿名用户'
        path = "{}/{}-{}".format(collection_title, title, author)
        print path
        try:
            if not os.path.exists(path):
                os.mkdir(path)
            num = 1
            for pic in content.xpath('//div[@class="RichContent-inner"]//img/@src'):
                if "whitedot" not in pic:
                    filename = "{}/{}.jpg".format(path, str(num))
                    self.saveImage(filename, pic)
                    num += 1
            print "{}   -----   图片已下载完成!".format(title)
        except Exception, e:
            print e

    def saveImage(self, filename, picPath):
        '''
        把图片下载到本地存储
        :param filename:
        :param picPath:
        :return:
        '''
        content = requests.get(picPath, headers=self.headers).content
        with open(filename, 'wb') as f:
            f.write(content)

    def workon(self):
        collectionNum = raw_input("请输入你要获取的收藏夹编号(比如:38624707):")
        pageNum = input("请输入你要爬取的页数:")
        for page in range(1, pageNum + 1):
            print "------------------------ 知乎图片爬虫开始启动 -----------------------"
            self.fromCollectionFindAnswer(str(collectionNum), str(page))
            print "------------------------ 第{}页爬取完成 -----------------------".format(page)

        print "所有爬取任务完成,Over..."


if __name__ == '__main__':
    spider = Zhihu()
    spider.workon()
