# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/20.
'''


'''
处理https请求ssl证书验证
'''
import requests
response = requests.get("https://www.baidu.com/", verify=True)

# 也可以省略不写
# response = requests.get("https://www.baidu.com/")
print response.text
