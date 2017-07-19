# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/3/19
"""

import commands


'''

1.commands.getstatusoutput('cmd')
此函数是返回命令执行返回值以及执行结果

'''

result1=commands.getstatusoutput('ls /Users/hushiwei/Downloads/learnsql')
print "result1 `s stutas : ",result1[0]
print "result1 `s output : ",result1[1]

'''
2.commands.getoutput('cmd')
此函数只返回结果,不返回返回值
'''

result2=commands.getoutput('ls /Users/hushiwei/Downloads/learnsql')
print result2


'''
3.commands.getstatus('file')
此函数返回ls -ld file 的执行结果

'''

result3=commands.getstatus('ls /Users/hushiwei/Downloads/learnsql')
print result3


sta,content=commands.getstatusoutput('java -version')
print str(sta)+" --- "+content[0:14]
