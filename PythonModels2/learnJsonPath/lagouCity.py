# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/7/24
"""
import urllib2
import json
import jsonpath

headers = {
    "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
}
url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'

request=urllib2.Request(url,headers=headers)
response=urllib2.urlopen(request)

html= response.read()

unicodestr=json.loads(html)

city_list=jsonpath.jsonpath(unicodestr,'$..name')
for item in city_list:
    print item

# 返回的是unicode字符串
array=json.dumps(city_list,ensure_ascii=False)
# array=json.dumps(city_list)

with open("json.txt","w") as f:
    f.write(array.encode("utf-8"))
