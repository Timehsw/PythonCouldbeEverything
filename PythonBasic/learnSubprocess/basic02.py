# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/4/9
"""
'''
调用 shell 命令
有 bug,如果输出内容增加，输出的问题本太长，会把管道给堵塞了
'''

import subprocess


def run_it(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True,
                         stderr=subprocess.PIPE, close_fds=True)
    print ('running:%s' % cmd)
    p.wait()
    if p.returncode != 0:
        print ("Non zero exit code:%s executing: %s" % (p.returncode, cmd))
    return p.stdout, p.stderr


out, err = run_it("ls -lh")
lines = out.readlines()

if not lines or len(lines) == 0:
    line = err.stderr.readlines()

print lines
