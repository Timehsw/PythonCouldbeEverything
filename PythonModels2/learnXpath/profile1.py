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
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'        }
url='https://www.zhihu.com/people/prog/followers'

response=requests.get(url,headers=headers).content
content=html.fromstring(response)
names=content.xpath('//div[@class="UserItem-title"]//a/text()')
for name in names:
    print name


