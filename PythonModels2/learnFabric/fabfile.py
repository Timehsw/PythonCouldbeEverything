# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/10/14.
'''
from fabric.api import env,run,local,runs_once,task
from fabric.operations import sudo


env.hosts=['importthis.top','69.112.67.133']
env.user='root'
env.password='xxxxxx'

@runs_once
def test_runonce():
    print "Hello Fabric! "
    run('uname -r')

@task
def testlocal():
    local('ls -l ~/')

@task
def test_task():
    local('pwd')
    run('pwd')

def testRemote():
    local("ls -l ~/demo")
    print "~"*100
    run('ls -l /root')
    print "-"*100

def deploy():
    test_task()

@task
def host_type():
    run('uname -r')