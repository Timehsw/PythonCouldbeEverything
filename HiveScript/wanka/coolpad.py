# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/4/9
"""
import datetime

def getDate(pastdays=7):
    today = datetime.date.today()
    print today.strftime("%Y%m%d")
    yesterday = today - datetime.timedelta(days=pastdays)
    yesterday = yesterday.strftime("%Y%m%d")
    print yesterday
    return yesterday


if __name__ == '__main__':
    getDate()
