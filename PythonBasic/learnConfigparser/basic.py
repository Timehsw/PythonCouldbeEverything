# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/4/9
"""
import subprocess
import ConfigParser


def readConfig(file="config.ini"):
    """Extract IP addresses and CMD from config file and retuen tuple"""
    ips = []
    dic={}
    config = ConfigParser.ConfigParser()
    config.read(file)
    print config.get('MACHINES','CENTOS')
    print "-----"
    machines = config.items("MACHINES")
    print machines
    commands = config.items("COMMANDS")
    print commands
    for ip in machines:
        dic[ip[0]]=ip[1]
        ips.append(ip[1])

    ip=config.items('test')
    print ip
    return dic


dic = readConfig()
print dic
print dic['centos']


