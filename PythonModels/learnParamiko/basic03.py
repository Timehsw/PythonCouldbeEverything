# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/4/8
"""
'''
:parameter是 ssh 连接模块
此例子用 ssh 连上远程服务器,
使用私钥连接
'''
import paramiko
import os

hostname = '10.10.25.11'
port = 22
username = 'root'
pkey_file='/root/.ssh/id_rsa'

if __name__ == '__main__':
    try:
        key=paramiko.RSAKey.from_private_key_file(pkey_file)
        s=paramiko.SSHClient()
        s.load_host_keys()
        s.connect(hostname,port,pkey=key)
        stdin,stdout,stderr=s.exec_command('ifconfig')
        print stdout.read()
    finally:
        s.close()
