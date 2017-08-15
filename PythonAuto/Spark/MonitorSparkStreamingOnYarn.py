# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/20.
'''
'''
通过调用yarn的rest接口,来监控sparkstreaming程序
'''
import json
import subprocess

apps = {
    "com.huanju.streaming.ADXStreaming": "sh ./start_adx_streaming_yarn.sh",
    "com.huanju.streaming.DSPStreaming": "sh ./start_dsp_streaming_yarn.sh",
    "com.huanju.streaming.CPDAppStreaming": "sh ./start_dsp_app_promotion_yarn.sh"
}


def run_it(cmd):
    '''
    通过python执行shell命令
    :param cmd:
    :return:
    '''
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True,
                         stderr=subprocess.PIPE)
    # print ('running:%s' % cmd)
    out, err = p.communicate()
    if p.returncode != 0:
        print ("Non zero exit code:%s executing: %s \nerr course ---> %s" % (p.returncode, cmd, err))
    return out


def runSparkStreaming(packageName):
    '''
    调用执行脚本
    :return:
    '''
    print "going to exec sparkstreaming program : %s" % packageName
    run_it(apps[packageName])


def collectPackageName(str):
    '''
    获取正则运行的所有包名
    :param str:
    :return:
    '''
    packages = {}
    obj = json.loads(str)
    apps = obj['apps']['app']
    for app in apps:
        packages[app['name']] = app['state']

    return packages


def findPackage(packageNames, packages):
    '''
    根据包名判断该程序是否正在运行中,
    若失败了,则执行重启任务的脚本
    :param packageNames: 需要监控的包名们(list,可以监控多个包)
    :param packages: yarn上正在执行的所有任务
    :return:
    '''
    for packageName in packageNames:
        if packageName in packages.keys():
            print packageName + " is: " + packages[packageName]
        else:
            print packageName + " is failed! "
            runSparkStreaming(packageName)


str = run_it(
    'curl --compressed -H "Accept: application/json" -X GET "http://master:8088/ws/v1/cluster/apps?states=RUNNING"')
packages = collectPackageName(str)

packageNames = ['com.huanju.streaming.DSPStreaming','com.huanju.streaming.CPDAppStreaming','com.huanju.streaming.ADXStreaming']
findPackage(packageNames, packages)
