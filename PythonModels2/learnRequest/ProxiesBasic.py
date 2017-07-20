# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/20.
'''

'''
request使用代理
'''


import requests

# 根据协议类型，选择不同的代理
proxies = {
  "http": "http://12.34.56.79:9527",
  "https": "http://12.34.56.79:9527",
}

response = requests.get("http://www.baidu.com", proxies = proxies)
print response.text