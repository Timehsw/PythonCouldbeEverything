# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/20.
'''

'''
web表单验证
'''

import requests

auth=('test', '123456')

response = requests.get('http://192.168.199.107', auth = auth)

print response.text