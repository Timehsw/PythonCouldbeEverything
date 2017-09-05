# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/9/5.
'''

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

print datetime.datetime.now()
print datetime.datetime.now().strftime('%H')

from datetime import datetime,timedelta,tzinfo

class GMT8(tzinfo):
    delta=timedelta(hours=8)

    def utcoffset(self,dt):
        return self.delta

    def tzname(self, dt):
        return "GMT+8"

    def dst(self,dt):
        return self.delta



class GMT(tzinfo):
    delta=timedelta(0)
    def utcoffset(self,dt):
        return self.delta
    def tzname(self,dt):
        return "GMT+0"
    def dst(self,dt):
        return self.delta



