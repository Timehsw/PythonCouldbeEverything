# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/20.
'''

import requests
import json
import time
import random
import hashlib


def getWord(jsonStr):
    obj = json.loads(jsonStr)
    arr = obj["smartResult"]['entries']
    for word in arr:
        print word


word = raw_input("请输入你要查询的英文:")
u = 'fanyideskweb'
f = str(int(time.time()*1000) + random.randint(1,10))
c = 'rY0D^0\'nM0}g5Mm1z%1G4'
sign = hashlib.md5((u + word + f + c).encode('utf-8')).hexdigest()


formdata = {
    "i": word,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": u,
    "salt": f,
    "sign": sign,
    "doctype": "json",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CL1CKBUTTON",
    "typoResult": "true"
}



headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
    "Cookie": "OUTFOX_SEARCH_USER_ID_NCOO=1198537320.275839; LAST_LOGIN=hsw_v5@163.com; _ga=GA1.2.1700165122.1495868452; JSESSIONID=aaaTEjvlWJvQTbFTM2D1v; SESSION_FROM_COOKIE=fanyiweb; OUTFOX_SEARCH_USER_ID=-902153939@111.193.196.253; _ntes_nnid=25e6900a08b62009ffbbd4006389c06b,1500518182363; ___rl__test__cookies=1500518210770"

}



url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=null"


response=requests.post(url,data=formdata,headers=headers)

content= response.text

getWord(content)
