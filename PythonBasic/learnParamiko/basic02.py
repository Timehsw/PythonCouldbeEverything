# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/4/8
"""
'''
:parameter是 ssh 连接模块
此例子用 ssh 连上远程服务器,在远程服务器上下载文件
使用 get()方法从远程主机上下载文件
使用 put()方法从 本地向远程主机上传文件
'''
import paramiko
import os

hostname = '10.10.25.11'
port = 22
username = 'root'
password = 'hadoopMhxzKhl'
dir_path='/home/root/statistics/dmp/dmp_asdk_appendCoolpadlog/wf/conf'

if __name__ == '__main__':
    try:
        t=paramiko.Transport((hostname,port))
        t.connect(username=username,password=password)
        sftp=paramiko.SFTPClient.from_transport(t)
        files=sftp.listdir(dir_path)
        for f in files:
            print 'Retreving',f
            sftp.get(os.path.join(dir_path,f),f)

    finally:
        t.close()
