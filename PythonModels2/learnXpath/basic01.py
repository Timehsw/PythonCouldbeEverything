# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/7/23
"""

import requests
from lxml import html
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}


url = 'https://download.postgresql.org/pub/repos/yum/9.2/redhat/rhel-7.3-x86_64/'

response = requests.get(url, headers=headers).content
content = html.fromstring(response)
names = content.xpath('//td[@class="n"]/a/@href')

print len(names)
for name in names:
    fullurl = url + name
    with open('links.txt', 'a') as f:
        print fullurl
        f.write(fullurl+"\n")

    f.close
