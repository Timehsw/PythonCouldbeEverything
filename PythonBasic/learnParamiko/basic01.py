# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/4/8
"""
'''
:parameter是 ssh 连接模块
此例子用 ssh 连上远程服务器,在远程服务器上执行命令,返回结果
'''
import paramiko

hostname = '10.10.25.11'
port = 22
username = 'root'
password = 'hadoopMhxzKhl'

if __name__ == '__main__':
    try:
        paramiko.util.log_to_file('paramiko.log')
        s = paramiko.SSHClient()
        s.load_system_host_keys()
        s.connect(hostname, port, username, password)
        stdin, stdout, stderr = s.exec_command('ifconfig')
        print stdout.read()
    finally:
        s.close()
