# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/20.
'''

import requests

formdata = {
    "i": "python",
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "1500518210777",
    "sign": "a2a93d46c0d3c725a3d06c31b8d9ddda",
    "doctype": "json",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CL1CKBUTTON",
    "typoResult": "true"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
}

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=null"

response = requests.post(url, data=formdata, headers=headers)

print response.text

# 如果是json文件可以直接显示
print response.json()
