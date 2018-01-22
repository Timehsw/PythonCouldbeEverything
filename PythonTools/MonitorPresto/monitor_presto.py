# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2018/1/22.
    fab -f monitor_presto.py deploy
    部署机器 10.10.25.204
# crontab 监控presto集群
*/10 * * * * source /root/.bash_profile;fab -f /root/prestomonitor/monitor_presto.py deploy > /root/prestomonitor/monitor.log
'''

from fabric.api import *
import time
import logging
import urllib2
import json
import os

with open("/root/prestomonitor/worker_of_presto") as f:
    content = [line.strip() for line in f]
env.hosts = content
env.user = 'xxx'
env.password = 'xxxxxxxxxx'

check_order = "ps -ef | grep presto | grep -v grep | awk '{print $2}'"
check_presto_isLive = "ps -ef | grep presto | grep -v grep | wc -l"

presto_folder = "/opt/presto-server-0.189"
restart_order = "source /home/presto/.bash_profile;bin/launcher restart"

wechats = "xxx|xxxx"


class WeChat(object):
    '''
    发送微信工具类
    '''

    def __init__(self, corpid, corpsecret, tokenpath):
        self.corpid = corpid
        self.corpsecret = corpsecret
        self.tokenpath = tokenpath
        self.logger = logging.getLogger('wechat')

    def saveToken(self):
        '''
        :return:
        '''
        try:
            with open(self.tokenpath, 'r') as f:
                token = f.read()
                if len(token) < 10:
                    token = self.getToken()
                    self.logger.info("Can not get token from %s,prepare to get token on api which token is %s" % (
                        self.tokenpath, token))
                    return token
                else:
                    return token
        except IOError:
            token = self.getToken()
            self.logger.info(
                "Can not get token from %s,prepare to get token on api which token is %s" % (self.tokenpath, token))
            return token

    def getToken(self):
        Url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (self.corpid, self.corpsecret)
        req = urllib2.Request(Url)
        result = urllib2.urlopen(req)
        json_access_token = json.loads(result.read())
        access_token = json_access_token['access_token']

        with open(self.tokenpath, 'w') as f:
            f.write(access_token)
        return access_token

    def setMessage(self, wechatids, text):
        token = self.saveToken()
        message = self.makeMessage(text)
        submiturl = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={0}'.format(token)
        data = {"touser": wechatids, "msgtype": "text", "agentid": "1000002", "text": {"content": message}, "safe": "0"}
        data = json.dumps(data, ensure_ascii=False)

        send_request = urllib2.Request(submiturl, data)

        self.logger.info("Send wechat %s" % text)

        response = json.loads(urllib2.urlopen(send_request).read())

        if response['errcode'] == 42001 or response['errcode'] == 40014:
            self.logger.info("Send wechat errorcode : %s" % response['errcode'])
            os.remove(self.tokenpath)
            self.setMessage(wechatids, text)

    def makeMessage(self, text):
        def date():
            date = time.strftime('%m-%d %H:%M:%S', time.localtime())
            return date

        return "%s \nCall Time:%s" % (text, date())


def check_presto():
    '''
    监控presto进程
    进程停止了则发微信通知,然后重启presto
    :return:
    '''
    with cd(presto_folder):
        current_host = env.host_string
        presto_process_num = run(check_order)
        presto_process_count = run(check_presto_isLive)
        if presto_process_count == "1":
            print "%s presto is running which process num is : %s" % (current_host, presto_process_num)
        else:
            print "%s presto process is stop, prepare to restart!" % current_host
            wechat_client = WeChat('xxxxxxxxx', 'xxxxxxxxxxxxxxxxxxxxxx',
                                   '/tmp/token.txt')
            wechat_client.setMessage(wechats, "%s presto process is stop, prepare to restart!" % current_host)
            run(restart_order)


@task()
def deploy():
    check_presto()
