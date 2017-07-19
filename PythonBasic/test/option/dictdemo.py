# -*- coding: utf-8 -*-
"""
Created by hushiwei on 16-12-25.
"""
import os
from datetime import datetime
a=9

def show():
    global a
    m={'a':4,'b':5,'c':'hello'}
    m['aa']=None
    for k,v in m.items():
        # print k,v
        tmp=str(k)+"="+str(v)+"&"
        print tmp
    # str=str+tmp


show()
