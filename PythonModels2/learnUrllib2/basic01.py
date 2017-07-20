# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/19.
'''

import urllib2

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=null&i=python&from=AUTO&to=AUTO&smartresult=dict&client=fanyideskweb&salt=1500518210777&sign=a2a93d46c0d3c725a3d06c31b8d9ddda&doctype=json&version=2.1&keyfrom=fanyi.web&action=FY_BY_CL1CKBUTTON&typoResult=true"
response=urllib2.urlopen(url)
print response.read()