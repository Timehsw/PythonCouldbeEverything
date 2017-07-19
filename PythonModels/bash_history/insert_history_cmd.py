#! /usr/bin/env python
# coding=utf-8
import os, sys, MySQLdb as mysql

if len(sys.argv) >= 1 and (sys.argv[1] == '--help' or sys.argv[1] == '-help'):
    print '-----example : python insert_history_cmd.py uid ctid cid path conn'
    os._exit(0)

length = len(sys.argv)
if length < 6:
    print 'error needs 5 args uid ctid cid path conn'
    os._exit(0)


# config
uid = sys.argv[1]
ctid = sys.argv[2]
cid = sys.argv[3]
file_path = sys.argv[4]
database_str = sys.argv[5].split(' ')

database_host = database_str[0]
database_user = database_str[1]
database_pass = database_str[2]
database_name = database_str[3]
database_port = int(database_str[4])




# init sqlcmd

data_list = []
try:
    file_object = open(file_path, 'r')
    lines = file_object.readlines()
    i = 0
    time_str = ''
    cmd_str = ''
    for line in lines:
        i += 1
        if i % 2 == 1:
            time_str = line.strip()[1:]
        else:
            cmd_str = line.strip()
            if len(time_str) >= 10:
                data_list.append((uid, ctid, cid, time_str,cmd_str))
except:
    pass

if len(data_list) > 0:
    conn = mysql.connect(host=database_host, user=database_user, passwd=database_pass, db=database_name,
                         port=database_port)
    cursor = conn.cursor()
    sqlcmd = "insert into command_history(user_id,course_training_id,container_id,execute_time,command) VALUES (%s,%s,%s,FROM_UNIXTIME(%s),%s)"
    try:
        cursor.executemany(sqlcmd, tuple(data_list))
        conn.commit()
    except Exception as e:
        print e
    finally:
        file_object.close()
        cursor.close()
        conn.close()
