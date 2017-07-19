# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/3/28
"""
'''
datetime模块定义了下面这几个类：

datetime.date：表示日期的类,
常用的属性有year, month, day；

datetime.time：表示时间的类,
常用的属性有hour, minute, second, microsecond；

datetime.datetime：表示日期时间,

datetime.timedelta：表示时间间隔，即两个时间点之间的长度

datetime.tzinfo：与时区有关的相关信息。
'''
import datetime


def getDate(pastdays=7):
    today = datetime.date.today()
    print today
    yesterday = today - datetime.timedelta(days=pastdays)
    print yesterday
    yesterday = yesterday.strftime("%Y%m%d")
    print yesterday
    return yesterday


getDate(1)

print (datetime.datetime.now()-datetime.timedelta(days=1)).strftime('%Y%m%d')
print (datetime.datetime.now()-datetime.timedelta(days=1))
print "now time is: ",datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')
print "now time is: ",datetime.datetime.now()
print "now time is: ",datetime.date.today()
print "now time is: ",datetime.date.today().strftime("%Y%m%d")
