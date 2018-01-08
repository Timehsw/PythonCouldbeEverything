#coding: utf-8 #############################################################
# File Name: main.py
# Author: mylonly
# mail: mylonly@gmail.com
# Created Time: Wed 11 Jun 2014 08:22:12 PM CST
#########################################################################
#!/usr/bin/python

import re,urllib2,HTMLParser,threading,Queue,time
import sys
reload(sys)
sys.setdefaultencoding('gb18030')

#各图集入口链接
htmlDoorList = []
#包含图片的Hmtl链接
htmlUrlList = []
#图片Url链接Queue
imageUrlList = Queue.Queue(0)
#捕获图片数量
imageGetCount = 0
#已下载图片数量
imageDownloadCount = 0
#每个图集的起始地址，用于判断终止
nextHtmlUrl = ''
#本地保存路径
localSavePath = 'D:\\data\\meinv\\'

#内页分析处理类
class ImageHtmlParser(HTMLParser.HTMLParser):
    def __init__(self):
        self.nextUrl = ''
        HTMLParser.HTMLParser.__init__(self)
    def handle_starttag(self,tag,attrs):
        global imageUrlList
        if(tag == 'img' and len(attrs) > 2 ):
            if(attrs[0] == ('id','bigImg')):
                url = attrs[1][1]
                imageUrlList.put(url)
                global imageGetCount
                imageGetCount = imageGetCount + 1
                print url
        elif(tag == 'a' and len(attrs) == 4):
            if(attrs[0] == ('id','pageNext') and attrs[1] == ('class','next')):
                global nextHtmlUrl
                if attrs[2][1]!='javascript:;':
                    nextHtmlUrl = attrs[2][1];



#首页分析类
class IndexHtmlParser(HTMLParser.HTMLParser):
    def __init__(self):
        self.urlList = []
        self.index = 0
        self.nextUrl = ''
        self.tagList = ['li','a']
        self.classList = ['photo-list-padding','pic']
        HTMLParser.HTMLParser.__init__(self)
    def handle_starttag(self,tag,attrs):
        if(tag == self.tagList[self.index]):
            for attr in attrs:
                if (attr[1] == self.classList[self.index]):
                    if(self.index == 0):
                        #第一层找到了
                        self.index = 1
                    else:
                        #第二层找到了
                        self.index = 0
                        print attrs[1][1]
                        self.urlList.append(attrs[1][1])
                        break
        elif(tag == 'a'):
            for attr in attrs:
                if (attr[0] == 'id' and attr[1] == 'pageNext'):
                    self.nextUrl = attrs[1][1]
                    print 'nextUrl:',self.nextUrl
                    break
#根据入口链接得到所有图片的url
class getImageUrl(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for door in htmlDoorList:
            print '开始获取图片地址,入口地址为:',door
            global nextHtmlUrl
            nextHtmlUrl = ''
            currentHtml=''
            while(door != ''):
                print '开始从网页%s获取图片...'% (host+door)
                if(nextHtmlUrl != ''):
                    request = urllib2.Request(host+nextHtmlUrl)
                else:
                    request = urllib2.Request(host+door)
                try:
                    m = urllib2.urlopen(request)
                    con = m.read()
                    imageParser.feed(con)
                    if currentHtml==nextHtmlUrl:
                        break
                    currentHtml=nextHtmlUrl
                    print '下一个页面地址为:',nextHtmlUrl
                    if(door == nextHtmlUrl):
                        break
                except urllib2.URLError,e:
                    print e.reason
        print '所有图片地址均已获得:',imageUrlList

class getImage(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global imageUrlList
        global imageDownloadCount
        print '开始下载图片...'
        while(True):
            print '目前捕获图片数量:',imageGetCount
            print '已下载图片数量:',imageDownloadCount
            image = imageUrlList.get()
            print '下载文件路径:',image
            try:
                cont = urllib2.urlopen(image).read()
                patter = '[0-9]*\.jpg';
                match = re.search(patter,image);
                if match:
                    print '正在下载文件：',match.group()
                    filename = localSavePath+match.group()
                    f = open(filename,'wb')
                    f.write(cont)
                    f.close()
                    #global imageDownloadCount
                    imageDownloadCount = imageDownloadCount + 1
                else:
                    print 'no match'
            except urllib2.URLError,e:
                print e.reason
        print '文件全部下载完成...'



#首页Hmtl解析器
indexParser = IndexHtmlParser()
#内页Html解析器
imageParser = ImageHtmlParser()

#根据首页得到所有入口链接
print '开始扫描首页...'
host = 'http://desk.zol.com.cn'
indexUrl = '/meinv/'
while (indexUrl != ''):
    print '正在抓取网页:',host+indexUrl
    request = urllib2.Request(host+indexUrl)
    try:
        m = urllib2.urlopen(request)
        con = m.read()
        indexParser.feed(con)
        if (indexUrl == indexParser.nextUrl):
            break
        else:
            indexUrl = indexParser.nextUrl
    except urllib2.URLError,e:
        print e.reason

print '首页扫描完成，所有图集链接已获得：'
htmlDoorList = indexParser.urlList



get = getImageUrl()
get.start()
print '获取图片链接线程启动:'

time.sleep(10)

download = getImage()
download.start()
print '下载图片链接线程启动:'