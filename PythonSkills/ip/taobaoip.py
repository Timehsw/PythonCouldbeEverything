# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/11/10.
    调用taobao的api查询ip地址
    通过python写alfred脚本,其中值得注意的是返回的内容必须拼接成josn格式进行返回
'''

import urllib2
import json

def json_feedback(ip,title,subtitle):
    argReturn="%s: %s %s " % (ip,title,subtitle)
    res={
        "title":title,
        "subtitle":subtitle,
        "arg":argReturn,
        "icon":"icon.png"
    }

    outputStr=json.dumps({"items":[res]})
    return outputStr

ip = u'221.223.164.136'
#ip = sys.argv[1]
ip_taobao_api_url = "http://ip.taobao.com/service/getIpInfo.php?ip="

f = urllib2.urlopen(ip_taobao_api_url + ip)

result = json.loads(f.read())
# return code: 0: success, 1: failed
#code result["code"]
area = result["data"]["area"]
city = result["data"]["city"]
country = result["data"]["country"]
isp = result["data"]["isp"]
region = result["data"]["region"]

title = "%s %s %s" % (country, region, city)
subtitle = "%s %s" % (area, isp)

print json_feedback(ip, title, subtitle)