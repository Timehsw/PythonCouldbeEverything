#coding:utf-8
'''
    Created on 2016/7/20 0020 
    @Author:   HuShiwei
'''
import json
objs=["hello","hehehh",3]
result=[]
for obj in objs:
    dic={}
    dic["tablename"]=obj
    dic["showname"]=obj
    dic["tableid"]=obj
    result.append(dic)



print json.dumps(result)