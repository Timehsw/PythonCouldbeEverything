# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2018/1/5.
    监控SparkStreaming程序
    一旦挂了,执行重启,同时发送邮件和微信报警
'''

import os
import subprocess
import json
import logging
import time
import urllib2
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

wechats = "HuShiwei"
sendEmails = ['hsw_v5@163.com', 'xxxx@gm825.com']

urlRun = 'curl --compressed -H "Accept: application/json" -X GET "http://u007:8089/ws/v1/cluster/apps?states=RUNNING"'
urlAcc = 'curl --compressed -H "Accept: application/json" -X GET "http://u007:8089/ws/v1/cluster/apps?states=ACCEPTED"'

monitorPrograms = {
    "com.huanju.streaming.ADXStreaming": "/home/hadoop/statistics/ad/adxstreaming/start_adx_streaming_yarn.sh",
    "com.huanju.online.streaming.DSPStreaming": "/home/hadoop/statistics/ad/dsp_ad_puton/dsp_ad_puton_streaming/start_dsp_streaming_yarn_test.sh",
    "com.huanju.streaming.CPDAppStreaming": "/home/hadoop/statistics/ad/dsp_app_promotion/start_dsp_app_promotion_yarn.sh"
}


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


class Message(object):
    '''
    构造邮箱发送的内容
    '''

    def format_str(self, strs):
        if not isinstance(strs, unicode):
            strs = unicode(strs)
        return strs

    def __init__(self, from_user, to_user, subject, content, with_attach=False):
        '''

        :param from_user: 谁发过来的邮件
        :param to_user: 发给谁
        :param subject: 邮件主题
        :param content: 邮件内容
        :param with_attach: 邮件是否包含附件
        '''

        if with_attach:
            self._message = MIMEMultipart()
            self._message.attach(MIMEText(content, 'plain', 'utf-8'))
        else:
            self._message = MIMEText(content, 'plain', 'utf-8')

        self._message['Subject'] = Header(subject, 'utf-8')
        self._message['From'] = Header(self.format_str(from_user), 'utf-8')
        self._message['To'] = Header(self.format_str(to_user), 'utf-8')
        self._with_attach = with_attach

    def attach(self, file_path):
        if self._with_attach == False:
            print "Please init the Message with attr 'with_attach = True'"
            exit(1)
        if os.path.isfile(file_path) == False:
            print "The file doesn`t exist!"
            exit(1)
        atta = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
        atta['Content-Type'] = 'application/octet-stream'
        atta['Content-Disposition'] = 'attachment; filename="%s"' % Header(os.path.basename(file_path), 'utf-8')
        self._message.attach(atta)

    def getMessage(self):
        return self._message.as_string()


class SMTPClient(object):
    '''
    发送邮件工具类
    '''

    def __init__(self, hostname, port, user, passwd):
        '''
        初始化相关参数
        :param hostname: QQ邮箱:smtp.qq.com
        :param port: QQ邮箱ssl加密端口:465
        :param user: QQ邮箱账号
        :param passwd: QQ邮箱授权秘钥,在web qq邮箱上获取
        '''
        self._HOST = hostname
        self._PORT = port
        self._USER = user
        self._PASS = passwd

    def send(self, receivers, msg):
        '''
        发送邮件方法
        :param receivers: 邮件接收者,可以是多个.为列表
        :param msg: 发送的邮件内容
        :return:
        '''
        if isinstance(msg, Message) == False:
            print "Error Message Instance!"
            exit(1)
        try:
            smtpObj = smtplib.SMTP_SSL(self._HOST, self._PORT)
            smtpObj.connect(self._HOST)
            smtpObj.login(self._USER, self._PASS)
            smtpObj.sendmail(self._USER, receivers, msg.getMessage())
            return (1, "邮件发送成功")
        except smtplib.SMTPException, e:
            return (0, "Error: 无法发送邮件%s" % e)


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


def reStartSparkScript(scriptPath):
    '''
    执行spark脚本
    1.cd到脚本所在路径
    2.在改路径执行脚本
    :param scripyPath:
    :return:
    '''
    logger = logging.getLogger("Main")
    scriptDir, script = os.path.split(scriptPath)
    os.chdir(scriptDir)
    run_it("sh %s" % script)
    logger.info("exec [ %s ] on [ %s ] " % (script, scriptDir))


def collectMonitorStatus(yarnRestApi):
    '''
    从Yarn的Running接口或者Accept接口中获取我们需要监控的程序状态
    :param str: yarn的running接口或者accept接口
    :return:
    '''
    strUrl = run_it(yarnRestApi)
    result = []
    obj = json.loads(strUrl)
    if obj['apps'] is None:
        return result
    else:
        apps = obj['apps']['app']
        result = [(app['name'], app['state']) for app in apps if app['name'] in monitorPrograms]
        return result


def checkMonitorApps():
    '''
    调用yarn的running接口和accept接口
    判断这里面是否有我们需要监控的spark程序
        如果没有就执行报警和重启
    :return:
    '''

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    logger = logging.getLogger("Main")

    smpt_client = SMTPClient('smtp.qq.com', 465, '694244330@qq.com', 'xxxxxx')
    wechat_client = WeChat('xxxxxxxxxxxxxx', 'xxxxxxxxxxxxxxxxxxxxxxxxx', '/tmp/token.txt')

    runningStatus = collectMonitorStatus(urlRun)
    acceptStatus = collectMonitorStatus(urlAcc)

    runningAcceptApps = dict(runningStatus + acceptStatus)

    logger.info("SparkStreaming ON Yarn Running And Accept ===>%s " % str(runningAcceptApps))

    for monitor in monitorPrograms:
        if monitor not in runningAcceptApps:
            logging.info("[ %s ] is not running or accept,prepare to restart!" % monitor)
            msg = Message("694244330@qq.com", "hushwiei", monitor, '%s is failed, prepare to resart! -- %s' % (
                monitor, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
            smpt_client.send(sendEmails, msg)
            wechat_client.setMessage(wechats, "%s is not running or accept,prepare to restart!" % monitor)
            reStartSparkScript(monitorPrograms[monitor])


def main():
    checkMonitorApps()


if __name__ == '__main__':
    main()
