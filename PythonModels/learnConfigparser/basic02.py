# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/4/9
"""
'''
多线程命令分发工具
'''
import subprocess
import ConfigParser
from threading import Thread
from Queue import Queue
import time

start = time.time()
queue = Queue()


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


def launcher(i, q, cmd):
    """Spaens command in a thread to an ip"""
    while True:
        # grabs ip,cmd from queue
        ip = q.get()
        print "Thread %s: Running %s to %s" % (i, cmd, ip)
        subprocess.call("ssh root@%s %s" % (ip, cmd), shell=True)
        q.task_done()


# grab ips and cmd from config
ips, cmds = readConfig()

# Determing Number of threads to use,but max out at 25
if len(ips) < 25:
    num_threads = len(ips)
else:
    num_threads = 25

# start thread pool

for i in range(num_threads):
    for cmd in cmds:
        worker = Thread(target=launcher, args=(i, queue, cmd))
        worker.setDaemon(True)
        worker.start()
print "Main Thread Waiting"
for ip in ips:
    queue.put(ip)
queue.join()
end = time.time()
print "Dispatch Completed in %s seconds" % end - start
