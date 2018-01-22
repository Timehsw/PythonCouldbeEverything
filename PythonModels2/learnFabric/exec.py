# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/10/17.
'''

from fabric.api import *
from fabric.contrib.files import *
from fabric.colors import green

env.hosts=['10.10.25.13']
env.user='root'
env.password='xxxxxxxxx'
local_path="~/demo"
remote_path="~/hsw/"
remote_dir_bak = "/home/root/statistics/auto_deploy_bak/"

def test():
    # 创建备份文件目录
    if not exists(remote_dir_bak):
        run("mkdir " + remote_dir_bak)
    run('uname -r')