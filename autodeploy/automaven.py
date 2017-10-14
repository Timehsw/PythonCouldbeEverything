#!/usr/bin/python
#-*- coding: utf-8 -*-  


import os
import sys
import subprocess
reload(sys)
sys.setdefaultencoding("utf-8")

with open('../path/svnpath.txt','r') as df:
    for svnpath in df.readlines():
        svnpath=svnpath.strip('\n')

appldr = {}
with open('../path/appldr.txt', 'r') as df:
   for kv in [d.strip().split(' ') for d in df]:
        appldr[kv[0]] = kv[1]

svnpath1 = {}
with open('../path/svnpath1.txt', 'r') as df:
   for kv in [d.strip().split(' ') for d in df]:
        svnpath1[kv[0]] = kv[1]
appname = list(svnpath1.keys())

svnpath2 = {}
with open('../path/svnpath2.txt', 'r') as df:
   for kv in [d.strip().split(' ') for d in df]:
       svnpath2[kv[0]] = kv[1]

svnpath3 = {}
with open('../path/svnpath3.txt', 'r') as df:
    for kv in [d.strip().split(' ') for d in df]:
       svnpath3[kv[0]] = kv[1]

# //检查svn版本
def svnup(p1,p2):
    try:
        local_rev = subprocess.check_output("svn info | awk '/^Last Changed Rev:/ {print $4}'", shell=True,cwd='../svnfiles/'+ p1 + '/Code/' + p2).strip()
        print("local_rev: " + local_rev)
    except:
        flag = 1
        return flag

    URL = subprocess.check_output("svn info | awk '/^URL:/ {print $2}'", shell=True,cwd='../svnfiles/'+ p1 + '/Code/' + p2).strip()
    print(URL)

    svn_cmd = "svn info "+URL+" | awk '/^Last Changed Rev:/ {print $4}'"
    svn_rev = subprocess.check_output(svn_cmd,shell=True,cwd='../svnfiles/'+ p1 + '/Code/' + p2).strip()
    print("svn_rev: " + svn_rev)
 
    if svn_rev == '':
        print("Get svn revision info fail")
    elif int(local_rev) < int(svn_rev):
        print("Need svn up")
        info = subprocess.check_output('svn up', shell=True,cwd='../svnfiles/'+ p1 + '/Code/' + p2)
        print(info)
        flag = 2
        return flag
    else:
        print(u"此程序不需要更新！！!")
        flag = 3
        return flag

def svn(p1,p2):
    flag = svnup(p1,p2)
    if flag == 1:
        f = 1
        os.system('cd ../svnfiles && svn checkout ' + svnpath + p1)
        return f
    elif flag == 2:
        f = 2
        print (u"已更新!!!")
        return f
    else:
        f = 3
        return f

# //maven自动打包
def automaven(appname,p1,p2,p3,appldr):
    os.system('cd ../svnfiles/' + p1 + '/Code/' + p2 + '&& mvn clean install -Dmaven.test.skip=true -Dmaven.javadoc.skip=true')
    os.system('cp -rf ../svnfiles/' + p1 + '/Code/' + p2 + '/' + p3 + '/target/*.tar.gz /opt/target/')
    os.system('fab -f putfiles.py put_task')
    os.system('fab -f autodeploy.py go:appname=' + appname + ',tar=' + p3 + ',appldr=' + appldr)

def autodeploy(appname,p3,appldr):
    os.system('fab -f autodeploy.py go1:appname=' + appname + ',tar=' + p3 + ',appldr=' + appldr)

def ps(appname,appldr):
    os.system('fab -f autodeploy.py ps_task:appname=' + appname +',appldr=' + appldr)

def psall(appname,appldr):
    os.system('fab -f autodeploy.py psall_task:appname=' + appname+ ',appldr=' + appldr)
	
def main():
    if sys.argv[1] == 'all':
        for i in appname:
            print i
            p1 = svnpath1[i]
            p2 = svnpath2[i]
            p3 = svnpath3[i]
            ldr = appldr[i]
            f = svn(p1,p2)
            if f == 1:
                os.system('echo '+ i+ ', > ../plog/alldeploy.txt')
                autodeploy(i,p3,ldr)
                psall(i,ldr)
            elif f == 2:
                os.system('echo '+ i +', >../plog/update.txt')
                automaven(i,p1,p2,p3,ldr)
                psall(i,ldr)
            else:
                os.system('echo '+ i+ ', >../plog/noupdate.txt ')
                continue
    else:
        for i in range(1,len(sys.argv)):
            print sys.argv[i]
            p1 = svnpath1[sys.argv[i]]
            p2 = svnpath2[sys.argv[i]]
            p3 = svnpath3[sys.argv[i]]
            ldr = appldr[sys.argv[i]]
            f = svn(p1,p2)
            if f == 1:
                os.system('echo '+ sys.argv[i]+ ', > ../plog/alldeploy.txt')
                autodeploy(sys.argv[i],p3,ldr)
                ps(sys.argv[i],ldr)
            elif f == 2:
                os.system('echo '+ sys.argv[i] +', >../plog/update.txt')
                automaven(i,p1,p2,p3,ldr)
                ps(sys.argv[i],ldr)
            else:
                os.system('echo '+ sys.argv[i]+ ', >../plog/noupdate.txt ')
                continue

if __name__ == '__main__':
    main()
