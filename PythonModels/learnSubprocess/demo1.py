# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/4/9
"""

import subprocess
import os


def run_it(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True,
                         stderr=subprocess.PIPE)
    print ('running:%s' % cmd)
    out, err = p.communicate()
    if p.returncode != 0:
        print ("Non zero exit code:%s executing: %s \nerr course ---> %s" % (p.returncode, cmd, err))
    return out


out = run_it('cd /Users/hushiwei/demo/auto_deploy;ls')
adx_sh = '/Users/hushiwei/demo/b.sh'
adx_dir = ''
for s in adx_sh.split('/')[0:-1]:
    adx_dir += s + '/'
print adx_dir
os.chdir(adx_dir)
os.getcwd()
res = os.system("sh b.sh")

print res

print "-------------------------------"

dic = {"a": (True, True), "b": (True, True)}

print dic['a'][0] | dic['a'][1]
print dic['a'][1]
print "----------------dic---------------"

apps = {
    "com.huanju.streaming.ADXStreaming": "sh ./start_adx_streaming_yarn.sh",
    "com.huanju.streaming.DSPStreaming": "sh ./start_dsp_streaming_yarn.sh",
    "com.huanju.streaming.CPDAppStreaming": "sh ./start_dsp_app_promotion_yarn.sh"
}

names=['com.huanju.streaming.ADXStreaming','com.huanju.streaming.CPDAppStreaming','bbb','ccc']
na='com.huanju.streaming.ADXStreamingaa'
print "-->",apps.has_key(na)

aa=[(name,"running") for name in names if apps.has_key(name)]

print aa