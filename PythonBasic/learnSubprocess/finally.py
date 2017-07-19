# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/4/9
"""

import subprocess


def run_it(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True,
                         stderr=subprocess.PIPE)
    print ('running:%s' % cmd)
    out, err = p.communicate()
    if p.returncode != 0:
        print ("Non zero exit code:%s executing: %s \nerr course ---> %s" % (p.returncode, cmd, err))
    return out


out = run_it("ls -lh ")
arr = out.split("\n")
for line in arr:
    print line
