# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/19.
'''

import urllib2

response=urllib2.urlopen("http://www.baidu.com")
print response.read()