# coding=utf8
__author__ = 'zenith'
import smtplib
import sys

from PythonTools.Email import MIMEText

content=sys.argv[1]
sender = 'wzhwei_test@sina.com'
receiver = 'wzhwei@126.com'
subject = '每日报错邮件'
smtpserver = "smtp.sina.com"
username = "wzhwei_test@sina.com"
password = "wzhwei_test_123"

msg = MIMEText(content,'html','utf-8')

msg['Subject'] = subject

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()