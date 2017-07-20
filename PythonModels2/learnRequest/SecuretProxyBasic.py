# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/20.
'''

'''
request使用私密代理
'''

import requests

# 如果代理需要使用HTTP Basic Auth，可以使用下面这种格式：
proxy = { "http": "mr_mao_hacker:sffqry9r@61.158.163.130:16816" }

response = requests.get("http://www.baidu.com", proxies = proxy)

print response.text
