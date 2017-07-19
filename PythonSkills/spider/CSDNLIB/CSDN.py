#coding:utf-8
'''
    Created on 2016/8/24 0024 
    @Author:   HuShiwei
'''
import urllib
import urllib2
import re
import MySQLdb
import datetime
# 57 58 59 60
class CSDN:
    def __init__(self):
        self.pageIndex = 57
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = { 'User-Agent' : self.user_agent }
        self.file=None
        self.defaultFileName='CSDNTitlesAboutSpark'
        self.pageContents=[]
    def getPage(self,pageIndex,pageNum):
        # url="http://lib.csdn.net/spark/node/"+str(pageIndex)
        try:
            url="http://lib.csdn.net/spark/node/"+str(pageIndex)+"?page="+str(pageNum)+"#md"
            request=urllib2.Request(url,headers=self.headers)
            response=urllib2.urlopen(request)
            pageCode= response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError,e:
            if hasattr(e,'reason'):
                print u'连接CSDN失败，错误原因',e.reason
                return None

    # pageNum
    def getPageNum(self,pageCode):
        pattern=re.compile(u'<div class="csdn-pagination.*?<input type="hidden".*?<b id="totalPage".*?<i>\\d*条(\\d*)页</i>.*?</span>',re.S)
        result=re.search(pattern,pageCode)
        if result:
            return result.group(1).strip()
        else:
            None


    # title introduction
    def getTitle(self,pageCode):
        pattern=re.compile('<div class="kn_right.*?<div class="rightcontent">.*?<div class="title"><a href="">(.*?)</a></div>.*?<div class="clearfix">.*?<p>(.*?)</p>',re.S)
        result=re.search(pattern,pageCode)
        if result:
            return result.group(1).strip(),result.group(2).strip()
        else:
            print "Nothing...."
            return None

    # 一个多少页，每页8个字段
    # nextArticleUrl  0
    # title   1
    # author  2
    # date  3
    # comeFromUrl  4
    # ParentCategory  5
    # relationUrl  6
    # ChildCategory  7
    # 2 1 3 0 5 4 7 6
    def getPageItems(self,pageCode):
        if not pageCode:
            print u"页面加载失败。。。"
        pattern=re.compile('<li class="clearfix c10">.*?<a contentId=".*?" href="(.*?)" title="(.*?)".*?</a>.*?<i>(.*?)</i>.*?class="content"><span>(.*?)&nbsp;&nbsp;</span>.*?<a href="(.*?)" target="_blank">(.*?)&nbsp;&nbsp;</a>.*?<a href="(.*?)" class="tabs" target="_blank">(.*?)</a>',re.S)
        items=re.findall(pattern,pageCode)

        for item in items:
            # print item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7]
            # print "\n"
            self.pageContents.append([item[2].strip(),item[1].strip(),item[3].strip(),item[0].strip(),item[5].strip(),item[4].strip(),item[7].strip(),item[6].strip()])
        return self.pageContents

    def getAllContent(self,pageIndex,pageNum):
        for i in range(pageNum):
            pageCode=self.getPage(pageIndex,i)
            self.getPageItems(pageCode)

        return self.pageContents

    def setFileName(self,title):
        if title is not None:
            self.file=open(title+".txt","w+")
        else:
            self.file=open(self.defaultFileName+".txt","w+")

    def writeData2Txt(self,allContent):
        print u"开始写入TxT...\n"
        print datetime.datetime.now()

        for i in range(len(allContent)):
            eachContent=allContent[i]
            eachline="\t".join(eachContent)
            self.file.write(eachline.encode('utf-8'))
            self.file.write("\n")
            self.file.flush()

        print u"写入完成..."
        print datetime.datetime.now()

    def writeData2MySQL(self,allContent):
        print u"开始写入Mysql数据库..."
        print datetime.datetime.now()
        db = MySQLdb.connect(host="192.168.15.15", user="root", passwd="5Rb!!@bqC%", db="sparkSQL",charset="utf8")
        db_cursor=db.cursor()

        for content in allContent:
            sql="""insert into CSDNSpark VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')""" %(content[0],content[1],content[2],content[3],content[4],content[5],content[6],content[7])
            db_cursor.execute(sql)
            # db_cursor.execute("insert into CSDNSpark VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')",content)

        db.commit()
        db_cursor.close()
        db.close()
        print u"写入完成..."
        print datetime.datetime.now()


    def start(self,pageIndex,flag):
        # 先抓取第一页内容，获取分类标题和简介
        pageCode=self.getPage(pageIndex,1)
        brief=self.getTitle(pageCode)
        pageNum=self.getPageNum(pageCode)
        title= brief[0]
        print u"Spark分类title: ",title
        print u"文章简介: ",brief[1]
        print u"一共 %d  页" %(int(pageNum))
        print u"-------------------准备写入-----------------------"
        allContent=self.getAllContent(pageIndex,int(pageNum))
        if flag==str(1):
            self.setFileName(title)
            self.writeData2Txt(allContent)
            self.file.close()
        else:
            self.writeData2MySQL(allContent)




csdn=CSDN()
print u"""
===============spark相关文章爬取====================
57
58
59
60
66
67
收录在以上页面了
"""

pageIndex=raw_input("请输入spark页面号: ")
flag=raw_input("1:写入到文本 2:写入到MySQL :")
csdn.start(pageIndex,flag)
# csdn.close()