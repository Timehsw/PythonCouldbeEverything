# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/3/20
"""
import subprocess

#call
# retcode = subprocess.call(["ls", "-l","/Users/hushiwei/IdeaProjects/PythonCouldbeEverything"])
#
# retcode1 = subprocess.call("ls -l /Users/hushiwei/IdeaProjects/PythonCouldbeEverything",shell=True)


# Popen
# child = subprocess.Popen(['ping','-c','4','blog.linuxeye.com'])
# child.wait()
# print 'parent process'
# print "-------------------------------------------------"
#
# child1=subprocess.Popen("ping -c4 blog.linuxeye.com",shell=True)
# print child1.pid
# child1.wait()
# print 'parent process....'
#
# print "-------------------------------------------------"


# child2=subprocess.Popen("ls -l /Users/hushiwei/IdeaProjects/PythonCouldbeEverything",shell=True,stdout=subprocess.PIPE)
# print child2.stdin
# print child2.stdout.read()
# print child2.stderr

print "-------------------------------------------------"
# communicate()是Popen对象的一个方法，该方法会阻塞父进程，直到子进程完成

# child1 = subprocess.Popen(["ls","-l"], stdout=subprocess.PIPE)
# print child1.stdout.read(),
# 或者
# child1.communicate()
# child1 = subprocess.Popen(["cat","/etc/passwd"], stdout=subprocess.PIPE)
# child2 = subprocess.Popen(["grep","0:0"],stdin=child1.stdout, stdout=subprocess.PIPE)
# out = child2.communicate()
#
# print out
# print "-------------------------------------------------"/


for i in range(10):
    child=subprocess.Popen(['ping','-c','4','www.baidu.com'])
    # if child.returncode==0:
    #     pass
    # print child.stdout.read()


print "------"
