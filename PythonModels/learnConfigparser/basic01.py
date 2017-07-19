# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/4/9
"""
import subprocess
import ConfigParser


def readConfig(file="config.ini"):
    """Extract IP addresses and CMD from config file and retuen tuple"""
    ips = []
    cmds = []
    config = ConfigParser.ConfigParser()
    config.read(file)
    machines = config.items("MACHINES")
    commands = config.items("COMMANDS")
    for ip in machines:
        ips.append(ip[1])
    for cmd in commands:
        cmds.append(cmd[1])
    return ips, cmds


ips, cmds = readConfig()

for ip in ips:
    for cmd in cmds:
        subprocess.call("ssh root@%s %s" % (ip, cmd), shell=True)
