#!/usr/bin/env python
#-*- coding: utf-8 -*-


from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm
from datetime import datetime 
import os

env.user='root'
env.hosts=['*.*.*.148']
env.password='******'

@task
def copy_task(appname,appldr):
    with cd(appldr):
        run('cp -rf ' + appname + ' ./bak/')

@task
def rm_task(appname,appldr):
    with cd(appldr + appname):
        run('rm -rf lib pay1paylib')

@task
def tar_task(appname,tar,appldr):
    with cd(appldr  + appname):
        run('tar -zxvf /vm_data/target/' + tar + '*.tar.gz lib pay1paylib')

@task
def restart_task(appname,appldr):
    with cd(appldr + appname + '/bin'):
        run('./restart.sh')

@task
def log_task(appname,appldr):
    with cd(appldr + appname):
        run('tail -f logs/' + appname + '.log -n200')

@task
def rollback_task(appname,appldr):
    with cd(appldr + appname):
        run('rm -rf pay1paylib')
	run('cp -rf ../bak/' + appname + '/pay1paylib ' + appldr + appname)

@task
def alltar_task(appname,tar,appldr):
    with cd(appldr):
        run('mkdir ' + appname)
        with cd(appname):
            run('tar -zxvf /vm_data/target/' + tar + '*.tar.gz')

@task
def ps_task(appname,appldr):
    a = run('ps -ef | grep '+ appname + '| grep -v grep | wc -l')
    if a > '0':
        pass
    else:
        local('echo '+ appname + ', > log.txt')
        rollback_task(appname,appldr)

@task
def psall_task(appname,appldr):
    a = run('ps -ef | grep '+ appname + '| grep -v grep | wc -l')
    if a > '0':
        pass
    else:
        local('echo '+ appname + ', > log.txt')

@task
def go(appname,tar,appldr):
    copy_task(appname,appldr)
    rm_task(appname,appldr)
    tar_task(appname,tar,appldr)
    restart_task(appname,appldr)
	
@task
def go1(appname,tar,appldr):
    alltar_task(appname,tar,appldr)
    restart_task(appname,appldr)
