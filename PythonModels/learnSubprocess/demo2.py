# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/4/9
"""

import subprocess
import os
import os

apps = {
    "com.huanju.streaming.ADXStreaming": "/home/hadoop/statistics/ad/adxstreamin/start_adx_streaming_yarn.sh",
    "com.huanju.online.streaming.DSPStreaming": "start_dsp_streaming_yarn.sh",
    "com.huanju.streaming.CPDAppStreaming": "start_dsp_app_promotion_yarn.sh"
}

running=[(u'com.huanju.streaming.CPDAppStreaming', u'RUNNING'), (u'com.huanju.online.streaming.DSPStreaming',u'RUNNING')]

# accept=[(u'com.huanju.streaming.ADXStreaming', u'ACCEPTED')]
accept=[]

allapp= running+accept

appdic= dict(allapp)


for app in apps:
    if app not in appdic:
        dir,script=os.path.split(apps[app])
        print dir
        print script



