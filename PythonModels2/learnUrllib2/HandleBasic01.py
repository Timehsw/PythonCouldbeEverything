# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/20.
'''

import urllib2

url="http://www.baidu.com"

# 先需要构造一个hander
handle=urllib2.HTTPHandler()

# 然后需要注册这个handle
opener=urllib2.build_opener(handle)

# 构造请求
resquest=urllib2.Request(url)

# 用handle打开请求
response=opener.open(resquest)
print response.read()
