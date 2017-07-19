#coding:utf-8
'''
    Created on 2016/8/24 0024 
    @Author:   HuShiwei
'''

import commands
import os
import MySQLdb
import json
# date=commands.getoutput("echo `date +%Y-%m-%d`")
# print date

def db_connect():
    conn =MySQLdb.connect(host='192.168.15.22',user='root',passwd='Jusfoun*',db='test')
    return conn
def db_disconnect(conn):
    conn.close()

def get_task_board():
    sql="select * from testSetOut"
    try:
        conn=db_connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        task={}
        for row in cursor.fetchall():
            tmp=json.loads("{}")
            print row
            tmp["id"]=row[0]
            tmp["result"]=row[1]

        task["json"]=json.dumps(tmp)

        print task
    except Exception, e:
        print e



get_task_board()