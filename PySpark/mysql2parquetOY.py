# -*- coding: utf-8 -*-
"""
Created by hushiwei on 16-12-20.
"""

import os
import smtplib
import sys

import MySQLdb
from PySpark.sql import SQLContext

from PythonModels.Email import MIMEText
from PySpark import SparkConf, SparkContext

reload(sys)
sys.setdefaultencoding('utf-8')
os.environ["SPARK_HOME"] = "/usr/hdp/2.4.0.0-169/spark"


class mysql2parquet():
    def __init__(self):
        self.sparkname = 'transform'
        self.hostname = "10.23.73.118"
        self.dbname = 'ouye'
        self.jdbcPort = '3306'
        self.properties = {
            "user": 'root',
            "password": 'jusfoun@123',
            "driver": 'com.mysql.jdbc.Driver'
        }
        self.mailto_list = ["hsw_v5@163.com"]
        self.mail_host = "smtp.qq.com"
        self.mail_user = "694244330"
        self.mail_pass = "tdjzzgfdiwgobehh"
        self.mail_postfix = "qq.com"
        self.database = MySQLdb.connect(host=self.hostname, user=self.properties.get('user'),
                                        passwd=self.properties.get('password'), db=self.dbname, charset="utf8")
        self.cursor = self.database.cursor()
        self.conf = SparkConf().setAppName(self.sparkname)
        self.sc = SparkContext(conf=self.conf)
        self.sqlContext = SQLContext(self.sc)

    def send_mail(self, to_list, sub, content):
        me = "Python Send Email" + "<" + self.mail_user + "@" + self.mail_postfix + ">"
        msg = MIMEText(content)
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ";".join(to_list)
        try:
            s = smtplib.SMTP_SSL(self.mail_host, 465)
            s.connect(self.mail_host)
            s.login(self.mail_user, self.mail_pass)
            s.sendmail(me, to_list, msg.as_string())
            s.close()
            return True
        except Exception, e:
            print str(e)
            return False

    def save_onetable(self, tablename):
        try:
            print "开始导入 %s ..." %(tablename)
            jdbcUrl = "jdbc:mysql://{0}:{1}/{2}?characterEncoding=utf8".format(self.hostname, self.jdbcPort,
                                                                               self.dbname)
            df = self.sqlContext.read.jdbc(url=jdbcUrl, table=tablename, properties=self.properties)
            # df.show()
            df.write.parquet("hdfs://ncp001/test/"+tablename)
            print "导入 %s 完成" % (tablename)
            # self.send_mail(self.mailto_list,"success","import success")
        except Exception, e:
            print str(e)
            self.send_mail(self.mailto_list, "loss", str(e))

    def save_alltables(self):
        try:
            self.cursor.execute('USE %s' %(self.dbname))
            self.cursor.execute('SHOW TABLES')
            tables = self.cursor.fetchall()
            print "库中一共有 %d 张表" % (len(tables))
            i = 0
            for table in tables:
                self.save_onetable(table[0])
                i += 1
            print "最后导入 %d 张表完成" % (i)
        except MySQLdb.Error, e:
            print "Mysql Error %d:%s" % (e.args[0], e.args[1])


if __name__ == '__main__':
    app = mysql2parquet()
    # app.save_onetable(sys.argv[1])
    app.save_alltables()
