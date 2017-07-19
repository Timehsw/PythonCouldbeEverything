# -*- coding: utf-8 -*-
"""
Created by HuShiwei on 2016/11/30 0030.
"""

import random
import datetime
import time

class appData(object):
    def __init__(self):
        self.area=["北京","天津","上海","重庆","河北","山西",
                   "辽宁","吉林","黑龙江","江苏","浙江","安徽",
                   "福建","江西","山东","河南","湖北","湖南",
                   "广东","海南","四川","贵州","云南","陕西",
                   "甘肃","青海","台湾","内蒙古","广西","西藏",
                   "宁夏","新疆","香港","澳门"]


    def sample_area(self):
        return random.choice(self.area)

    def sample_uid(self):
        code=str(random.randrange(1,1000,1))
        return "user"+code

    def sample_request(self):
        return random.randrange(1,300,1)

    def sample_appid(self):
        id=str(random.randrange(1000,2000,1))
        return "IME"+id

    def sample_service(self):
        id=str(random.randrange(1,40,1))
        return "service"+id

    def sample_time(self):
        print datetime.datetime.now()
        print datetime.time.tzname()
        print time.time()

    def sampleData(self,count=10):
        while count>0:
            area=self.sample_area()
            uid=self.sample_uid()
            request=self.sample_request()
            appid=self.sample_appid()
            service=self.sample_service()
            msg="{appid} {service} {area} {uid} {request}"


app=appData()
# print app.sample_area()
# print app.sample_uid()
# print app.sample_request()
# print app.sample_appid()
# print app.sample_service()
app.sample_time()