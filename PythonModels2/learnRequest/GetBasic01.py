# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/20.
'''

import requests

# get请求

url="http://master:8088/cluster/apps/RUNNING"
response=requests.get(url)

# 也可以这样写

response=requests.request("get",url)

# 添加header方法和查询参数

kw={'wd':"三国演义"}
headers={
    "User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
}

response=requests.get(url+"s?",params=kw,headers=headers)

# 查看响应内容,返回的是Unicode格式的数据
print response.text

# 查看响应内容,返回的的字节流数据
print response.content

# 查看完整的url地址
print response.url

# 查看响应头部字符编码
print response.encoding

# 查看响应码
print response.status_code


