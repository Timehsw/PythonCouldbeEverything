# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/8/18.
'''

import requests
import time

str = r'{"reportData":{"package":"com.huanju.asdkdemo"},"reportType":0,"sign":"a685a57b65238c258d45810f2430a5ff"}'

url = "http://package.mhacn.net/api/delay/report/download/start?app_id=b1002b&channel_id=20002b&svr=1.3.0&pkg=com.huanju.msdk&svc=5&nonce=1503994276&cuid=CF4E1921E277396889A0D821A8B5A59D&ovr=7.0&device=Xiaomi_MI+5&net_type=1&client_id=861322039795741&info_ms=u6fK0dta2OU0SGxmkj%2BPPw%3D%3D&info_ma=6tgzOm%2BevOdfWaHlk36e9WdZnSQVkGzIXcLU7QEOhl0%3D&mno=0&info_la=z%2FpM5uqCi3FXdbGD9FsQfw%3D%3D&info_ci=z%2FpM5uqCi3FXdbGD9FsQfw%3D%3D&mcc=0&clientversion=v1.1&bssid=Xa502KAPAYRe%2BmRVz60AOzlTCjFRZ%2FozuYtTMYwqzKw%3D&os_level=24&os_id=ebad08dc039bd55d&resolution=1080_1920&dpi=480&client_ip=10.0.0.111&pdunid=c5693424"


def request():
    response = requests.post(url, data=str)

    print response.text


def workon(nums):
    for i in range(nums):
        request()
        time.sleep(1)


def loop():
    for i in range(100):
        workon(100)
        time.sleep(1)



loop()