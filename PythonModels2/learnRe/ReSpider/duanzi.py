# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/21.
'''
'''
简单爬虫,运用正则爬取段子
'''
import urllib2
import re


class Duanzi:
    def __init__(self):
        self.page = 1
        self.switch = True

    def loadPage(self):
        '''

        获取网页内容
        :return: 返回匹配到的段子
        '''

        url = 'http://www.neihan8.com/article/list_5_' + str(self.page) + '.html'
        headers = {
            "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
        }
        try:
            request = urllib2.Request(url=url, headers=headers)
            html = urllib2.urlopen(request).read().decode('gbk').encode('utf-8')
            pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>', re.S)
            contents = pattern.findall(html)
            self.dealContent(contents)
        except urllib2.HTTPError,e:
            print e.code
            print e


    def dealContent(self, contents):
        '''
        对匹配到的段子进行一些处理
        :param contents:
        :return:
        '''

        for content in contents:
            content = content.replace("<br />", "").replace("<p>", "").replace("</p>", "")
            self.saveContent(content)
            print "spider running page %s" % self.page
        print "page %s over..." % self.page

    def saveContent(self, content):
        '''
        存储爬取到的段子内容
        :param content:
        :return:
        '''
        with open("duanzi.txt", 'a') as file:
            file.write(content)

    def workon(self):
        '''
        爬虫的运行方法类
        :return:
        '''
        while self.switch:
            command = raw_input("输入回车继续爬取,输入(quit)爬虫退出:")
            if command == 'quit':
                self.switch = False
                print "Spider is end..."
                # break
            else:
                self.loadPage()
                self.page += 1


if __name__ == '__main__':
    spider = Duanzi()
    spider.workon()
