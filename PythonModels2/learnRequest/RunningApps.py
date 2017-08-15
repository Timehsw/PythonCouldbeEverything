# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/8/15.
'''
import requests
from lxml import html
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

headers={
    "User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "Accept":"application/json"
}

url='http://master:8088/cluster/apps/RUNNING?'
kw={'states':"RUNNING"}

response=requests.get(url,params=kw,headers=headers).content

print response

'''
print content
names=content.xpath('//tr[@class="even"]/td[3]')
for name in names:
    print name

'''