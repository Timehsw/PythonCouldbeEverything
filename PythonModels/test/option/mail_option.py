# coding=utf-8
__author__ = 'zenith'

import smtplib

from PythonSkills.Email import MIMEText

sender = "wzhwei_test@sina.com"
reciever = "wzhwei@126.com"
subject = "test sub"
smtpserver = "smtp.sina.com"
username = "wzhwei_test@sina.com"
password = "wzhwei_test_123"
msg = MIMEText("<html>this is 邮件内容</html>", "html", "utf-8")

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, reciever, msg.as_string())
smtp.quit()
