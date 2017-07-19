# -*- coding: utf-8 -*-
"""
Created by hushiwei on 16-12-21.
"""

def show():
    try:
        tmp="\u8457\u4f5c\u6743\u4eba(\u56fd\u7c4d)"
        print tmp
        m={
            'a':9,
            'b':10
        }
        print m['a']
        print m.get('a')
        print m['c']
        # print m.get('c')
        a=9
        b=0
        c=a/b

    except Exception,e:
        print str(e)

show()
