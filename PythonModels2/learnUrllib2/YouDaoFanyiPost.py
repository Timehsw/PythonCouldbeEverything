# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/20.
'''

import urllib
import urllib2
import json


def getWord(jsonStr):
    obj = json.loads(jsonStr)
    arr = obj["smartResult"]['entries']
    for word in arr:
        print word


header = {
    "Accept": " application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": " XMLHttpRequest",
    "User-Agent": " Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Language": " zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
    "Cookie": " OUTFOX_SEARCH_USER_ID_NCOO=1198537320.275839; LAST_LOGIN=hsw_v5@163.com; _ga=GA1.2.1700165122.1495868452; JSESSIONID=aaaTEjvlWJvQTbFTM2D1v; SESSION_FROM_COOKIE=fanyiweb; OUTFOX_SEARCH_USER_ID=-902153939@111.193.196.253; _ntes_nnid=25e6900a08b62009ffbbd4006389c06b,1500518182363; ___rl__test__cookies=1500518210770"

}

word = raw_input("请输入你要查询的英文:")
formdata = {
    "i": word,
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

data = urllib.urlencode(formdata)

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=null"

request = urllib2.Request(url=url, data=data, headers=header)
response = urllib2.urlopen(request)
wordC = response.read()
print wordC
getWord(wordC)
