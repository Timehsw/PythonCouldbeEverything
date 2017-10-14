#!/usr/bin/env python  
#-*- coding: utf-8 -*-  


from fabric.api import *  
from fabric.context_managers import *  
from fabric.contrib.console import confirm  
  
env.user='root'
env.hosts=['*.*.*.148']
env.password='******'  

# //将target包推送到目标机
@task
def put_task():    
    with cd("/opt/target"):  
        with settings(warn_only=True):  
            result = put("/opt/target/*.tar.gz", "/vm_data/target/")  
        if result.failed and not confirm("put file failed, Continue[Y/N]?"):  
            abort("Aborting file put task!")  
 
# //校验md5值
@task  
def check_task():  
    with settings(warn_only=True):  
        lmd5=local("md5sum /opt/target/*.tar.gz",capture=True).split(' ')[0]  
        rmd5=run("md5sum /opt/target/*.tar.gz").split(' ')[0]  
    if lmd5==rmd5:  
        print "OK"  
    else:  
        print "ERROR"  
   
@task  
def go():  
    put_task()  
    check_task() 
