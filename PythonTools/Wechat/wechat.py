#! /usr/bin/env python
# -*- conding:utf-8 -*-


import json
import warnings
import sys
import time
import urllib, urllib2
import logging


class WeChat(object):
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
        message = self.content(text)
        submiturl = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={0}'.format(token)
        data = {"touser": wechatids, "msgtype": "text", "agentid": "1000002", "text": {"content": message}, "safe": "0"}
        data = json.dumps(data, ensure_ascii=False)

        send_request = urllib2.Request(submiturl, data)

        self.logger.info("Send wechat %s" % text)

        response = json.loads(urllib2.urlopen(send_request).read())

        if response['errcode'] == 42001 or response['errcode'] == 40014:
            self.setMessage(wechatids, message)

    def content(self, content):
        def date():
            date = time.strftime('%m-%d %H:%M:%S', time.localtime())
            return date

        return "%s \nCall Time:%s" % (content, date())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    wechatClient = WeChat('xxxxxxxxxx', 'xxxxxxxxxxxxxxxx', '/tmp/token.txt')
    userid = "HuShiWei"
    text = "123456777"

    wechatClient.setMessage(userid, text)
