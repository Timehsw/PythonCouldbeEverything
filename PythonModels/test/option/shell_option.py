# coding=utf-8
__author__ = 'zenith'
# 1

import os, commands

# print("os.system", os.system('cat /etc/cpuinfo'))
# print("os.system", os.system('sh /root/hello.sh'))
#
# print("os.popen", os.popen('cat /etc/cpuinfo').read())
# print("os.popen", os.popen('sh /root/hello.sh').read())
#
# print("commands", commands.getstatusoutput('ll'))
# print("commands", commands.getstatusoutput('sh /root/hello.sh'))
result=commands.getoutput('df -h')
type(result)
print result
print commands.getstatusoutput('pwd')[1]




