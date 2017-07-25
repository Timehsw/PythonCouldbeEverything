# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/25.
'''
'''
获取糗事百科的段子
'''

import requests
from lxml import html
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')
class Qiushi():
    def __init__(self):
        self.url = "http://www.qiushibaike.com/8hr/page/"
        self.headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    def loagPage(self,page):
        url=self.url+str(page)+"/"
        text=requests.get(url,headers=self.headers).text
        content_text=html.fromstring(text)

        # 获取所有的段子节点
        node_list=content_text.xpath('//div[contains(@id,"qiushi_tag")]')
        for node in node_list:
            username= node.xpath('.//h2/text()')[0].encode('utf-8')
            content=node.xpath('.//div[@class="content"]/span/text()')[0]
            vote=node.xpath('./div[@class="stats"]/span[@class="stats-vote"]/i/text()')[0]
            commentNum=node.xpath('./div[@class="stats"]/span[@class="stats-comments"]//i/text()')[0]
            item={
                "username":username,
                "content":content,
                "vote":vote,
                "commentNum":commentNum
            }
            with open('qiushiduanzi.json','a') as f:
                f.write(json.dumps(item,ensure_ascii=False)+"\n")


    def workon(self):
        pages=input("请输入你要爬取的页数:")
        for page in range(1,pages+1):
            self.loagPage(page)
            print "第%d页爬取完成" % page
        print "全部爬取完成..."





if __name__ == '__main__':
    spider=Qiushi()
    spider.workon()
