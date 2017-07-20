# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/20.
'''

import json

str='''{"translateResult":["python"],"errorCode":0,"type":"en2zh-CHS","smartResult":{"entries":["","n. 巨蟒；大蟒","n. （法）皮东（人名"],"type":1}}'''


obj=json.loads(str)


print obj.keys()

arr= obj["smartResult"]['entries']

for word in arr:
    print word