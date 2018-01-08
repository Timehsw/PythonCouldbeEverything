# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/12/29.
    发送邮件工具类
    1.构造邮件内容类Message
    2.发送邮件工具类SMTPClient

    发送网易企业邮箱

    https://qiye.163.com/entry/help/help-client.htm

'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os


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


if __name__ == '__main__':
    smpt_client = SMTPClient('smtp.qiye.163.com', 994, 'xxxx@gm825.com', 'xxxx')
    msg = Message("hushiwei@gm825.com", 'Kindle', '菊与刀.mobi', '菊与刀.mobi')
    print msg.getMessage()
    print smpt_client.send(['hsw_v5@163.com'], msg)

    # smpt_client = SMTPClient('smtp.qq.com', 465, 'hushiwei@gm825.com', 'hsw_0724')
    # msg = Message("694244330@qq.com", 'Kindle', '张飞流水账.mobi', '张飞流水账.mobi', with_attach=True)
    # msg.attach("./张飞流水账.mobi")
    # print msg.getMessage()
    # print smpt_client.send(['hsw_v5@163.com', 'hushiwei@gm825.com'], msg)
