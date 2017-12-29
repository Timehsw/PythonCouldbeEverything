#! /usr/bin/env python
# -*- conding:utf-8 -*-


import json
import warnings
import sys
import time
import urllib, urllib2


def gettoken(corpid, corpsecret, tokenpath):
    # print corpid
    Url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (corpid, corpsecret)
    req = urllib2.Request(Url)
    result = urllib2.urlopen(req)
    json_access_token = json.loads(result.read())
    access_token=json_access_token['access_token']
    print "get methods ---> access_token:%s"%access_token

    with open(tokenpath, 'w') as f:
        f.write(access_token)
    return access_token


def sendmessage(Userid, Text, token):
    submiturl = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={0}'.format(token)
    data = {"touser": Userid, "msgtype": "text", "agentid": "1000002", "text": {"content": Text}, "safe": "0"}
    data = json.dumps(data, ensure_ascii=False)

    send_request = urllib2.Request(submiturl, data)

    response = json.loads(urllib2.urlopen(send_request).read())
    print response

    if response['errcode'] == 42001 or response['errcode'] == 40014:
        token = gettoken('xxxxxx', 'xxxxxxxxxxxxxxxxxx', '/tmp/token.txt')
        sendmessage(Userid, Text, token)


def readtoken(corpid, corpsecre, tokenpath):
    try:
        with open(tokenpath, 'r') as f:
            token = f.read()
            if len(token)<10:
                token = gettoken(corpid, corpsecre, tokenpath)
                return token
            else:
                return token
    except IOError:
        token = gettoken(corpid, corpsecre, tokenpath)
        return token


def date():
    date = time.strftime('%m-%d %H:%M:%S', time.localtime())
    return date


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    token = readtoken('xxxxxxxx', 'xxxxxxxxxxxxxxxxxxx', '/tmp/token.txt')
    userid = sys.argv[1]
    text = sys.argv[2] + '\nCall Time:' + date()

    print "argv-->"+str(userid)+"-->"+str(text)

    sendmessage(str(userid), str(text), token)