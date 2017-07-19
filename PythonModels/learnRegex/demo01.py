#coding:utf-8
'''
    Created on 2016/8/15 0015 
    @Author:   HuShiwei
'''
import re
str="""in24.inetnebr.com - - [01/Aug/1995:00:00:01 -0400] "GET /shuttle/missions/sts-68/news/sts-68-mcc-05.txt HTTP/1.0" 200 1839"""

print str

compile_pattern=re.compile(r'^.*\[(\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2} -\d{4})]')
result1=compile_pattern.match(str)
print result1.group(1)
result2=re.match(r'^([^\s]+\s)',str)
print result2.group(1)