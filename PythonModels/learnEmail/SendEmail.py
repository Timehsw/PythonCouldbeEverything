# -*- coding: utf-8 -*-
"""
Created by hushiwei on 16-12-19.
"""

#==========================================
# 导入smtplib和MIMEText
#==========================================
import smtplib

from email.mime.text import MIMEText

#==========================================
# 要发给谁，这里可以是多个人，写在列表里即可
#==========================================
mailto_list=["hsw_v5@163.com","hushiwei@gm825.com"]
#==========================================
# 设置服务器，用户名、口令以及邮箱的后缀。这里qq的邮箱密码，必须得是秘钥，得通过验证后才能获取。具体看QQ邮箱的
#==========================================
mail_host="smtp.qq.com"
mail_user="694244330"
mail_pass="****************"
mail_postfix="qq.com"
#==========================================
# 发送邮件
#==========================================
def send_mail(to_list,sub,content):
    '''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("aaa@126.com","sub","content")
    '''
    me="Python Send Email"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        # s = smtplib.SMTP()
        s = smtplib.SMTP_SSL(mail_host,465)
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    if send_mail(mailto_list,"here is subject","here is content"):
        print "发送成功"
    else:
        print "发送失败"