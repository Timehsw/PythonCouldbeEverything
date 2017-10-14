# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/10/14.
    多服务器并且,并且多服务器的密码不一样的时候,我必须把端口也加上
    这样我才可以不用输入密码
'''

from fabric.api import env,run,roles,execute
from fabric.colors import *

# 给服务器分组,不同组的服务器做不同的事情
env.roledefs={
    'vps':['root@importthis.top:22','root@69.112.67.133:22'],
    'aliyun':['root@114.25.117.65:22'],
}

# env.hosts=[
#     'root@importthis.top:22',
#     'root@69.112.67.133:22',
#     'root@114.25.117.65:22',
# ]
env.passwords={
    'root@importthis.top:22':'xxx',
    'root@69.12.67.133:22':'xxx',
    'root@114.215.117.65:22':'xxx',
}

@roles('vps')
def task1():
    print red("execute task1...")
    run('hostname')

@roles('aliyun')
def task2():
    print blue("execute task2...")
    run('uname -r')


def dotask():
    execute(task1)
    execute(task2)