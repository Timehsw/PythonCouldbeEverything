# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/19.
'''

'''
python get请求

'''
import urllib
import urllib2

kw={"wd":"三国演义"}
key_words=urllib.urlencode(kw)
url="http://www.baidu.com/s"
realUrl=url+"?"+key_words

print realUrl

header={
    "User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
}

resquest=urllib2.Request(realUrl,headers=header)
response=urllib2.urlopen(resquest)

print response.read()