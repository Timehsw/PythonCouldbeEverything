# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/23.
'''

import requests
from lxml import html

#


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
    "Cookie": 'd_c0="ACCCItg0bguPTuSWzkKoBlPEFSv_VHbV4f4=|1489154388"; _zap=a1cd94b2-4f86-4883-917b-3915b8cb26e9; _ga=GA1.2.1981484424.1494568992; r_cap_id="NzQxYTE5MGNiNTE4NDk5Mjg4M2FjZTJjMGE1ZjM2NTc=|1498541307|3757c40a1662d8408b6edf67f352361bb24a81e2"; cap_id="MGI3ZDQwOWI4ZWY2NGZkNDkyZDVmMDdiZDk3ZmI5NWM=|1498541307|4bcc436cdfa7cbddf850f22cbf2a0813d527dbc7"; z_c0=Mi4wQUFDQWViRWNBQUFBSUlJaTJEUnVDeGNBQUFCaEFsVk5fbmw1V1FEeEFKcU9fV05IT3hXbk1oU05xVXdqazFKZk9B|1498541310|abb3f10588b5aaf8629f9c3b908fc96ee07010a2; q_c1=2343456a6f4546169eff16afd3ca3eda|1500188880000|1489154388000; q_c1=2343456a6f4546169eff16afd3ca3eda|1500188880000|1489154388000; aliyungf_tc=AQAAAPpv11DjqwEAAS10e/kIN5mMraiF; _xsrf=21251e64-0e14-487d-ade9-ec26e3b48d7c; __utma=51854390.1981484424.1494568992.1500603028.1500734369.2; __utmb=51854390.0.10.1500734369; __utmc=51854390; __utmz=51854390.1500734369.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100-1|2=registration_date=20130729=1^3=entry_date=20130729=1'
}


response=requests.get("https://www.zhihu.com/people/hsw_v5/following?page=2",headers=headers).content

content=html.fromstring(response)
print content

# 取每页关注者的名字
# arr=content.xpath('//div[@class="ContentItem-head"]')
arr=content.xpath('//div[@class="List-item"]//div[@class="ContentItem-head"]//a/text()')

for item in arr:
    print item
    # print item.xpath('//h2[@class="ContentItem-title"]//a[@class="UserLink-link"]/@href')