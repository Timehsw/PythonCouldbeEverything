# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/7/20
"""
import urllib2

httpHandler=urllib2.HTTPHandler()

opener=urllib2.build_opener(httpHandler)

request=urllib2.Request("http://www.baidu.com")

response=opener.open(request)

print response.read()