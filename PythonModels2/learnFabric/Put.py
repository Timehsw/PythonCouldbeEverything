# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/10/14.
'''

from fabric.api import env,run,local,runs_once,task,put,lcd,cd,settings,abort
from fabric.operations import sudo
from fabric.context_managers import *
from fabric.contrib.console import confirm
from fabric.colors import *

# env.hosts=['importthis.top','69.112.67.133']
env.hosts=['importthis.top']
env.user='root'
env.password='xxx'

# 打包文件
@runs_once
def tar_task():
    with lcd('/Users/hushiwei'):
        local('tar -czf demo.tar.gz demo')
# 上传文件
def put_task():
    run('mkdir -p /root/fabrictest/tarfile')
    with cd('/root/fabrictest/tarfile'):
        with settings(warn_only=True):
            result=put('/Users/hushiwei/demo.tar.gz','/root/fabrictest/tarfile/')
        if result.failed and not confirm("put file failed,Continue[Y/N]?"):
            abort("Aborting file put task!")


# 校对文件
def check_task():
    with settings(warn_only=True):
        lmd5=local('md5 /Users/hushiwei/demo.tar.gz',capture=True).split('=')[1].strip()
        rmd5=run('md5sum /root/fabrictest/tarfile/demo.tar.gz').split(' ')[0].strip()

    if lmd5==rmd5:
        print yellow('check OK! File Put Successful!')
    else:
        print red('check ERROR! File Put Failed!')

def go():
    tar_task()
    put_task()
    check_task()

# 校对文件