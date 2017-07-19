# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/3/28
"""

#coding:utf-8

import commands
from xmlrpclib import ServerProxy
import  multiprocessing
import time
import ftplib
import os
import socket
import datetime

HOST = 'xxx.xxx.xxx.xxxx'
DIRN = ''
USER_NAME = 'xxx'
PWD = 'xxx'

def DownloadFile(ftp_file, local_file):
    try:
        f = ftplib.FTP(HOST)
    except(socket.error, socket.gaierror) as e:
        print('ERROR:cannot reach %s' % HOST)
        return -1
    print('*** Connected to host %s' % HOST)

    try:
        f.login(USER_NAME, PWD)
    except ftplib.error_perm:
        print('ERROR:cannot login USER_NAME=%s, PWD=%s' % (USER_NAME, PWD))
        f.quit()
        return -1
    print('*** Logined in as %s' % USER_NAME)

    try:
        #f.cwd(DIRN)
        print "call f.cwd"
    except ftplib.error_perm:
        print('ERROR:cannot CD to %s' % DIRN)
        f.quit()
        return -1

    try:
        file = open(local_file, 'wb')
        f.retrbinary('RETR %s' % ftp_file, file.write, 10240)
        file.close()

    except ftplib.error_perm:
        print('ERROR:cannot read file %s' % ftp_file)

        os.unlink(ftp_file)
        file.close()
        return -1
    else:
        print('*** Downloaded %s to %s' % (ftp_file, os.getcwd()))
    f.quit()

    return 0



def launch_task(pday, handler, files):
    print "pday=%s, files=%s" % (pday, files)
    print "remote dump start ..."
    print handler.dump_files(files, pday)
    print "remote task start ..."
    print handler.start()

def lauch_local_task(pday, local_list_files):
    print "local start ..."
    local_source_path = "/data/users/data-warehouse/zmtech/source/pday=%s" % pday
    commands.getoutput("mkdir -p %s" % local_source_path)
    commands.getstatusoutput("hadoop fs -get %s %s" % (local_list_files, local_source_path))
    print "local task start..."
    commands.getoutput("sh /data/users/data-warehouse/zmtech/start.sh %s" % pday)

def task_status(pday):
    import commands
    path = "/data/users/data-warehouse/zmtech/result/pday=%s" % pday
    file_arr = commands.getoutput("ls %s" % path).split("\n")
    ret = 0
    #print "file_arr... "
    #print file_arr
    for file in file_arr:
        #print "fname = %s" % file
        if "tmp" in file.strip():
            print "...........filename=%s......." % file_name
            ret = -1
            break

    print "ret = %s" % ret

    return ret

def upload_files(pday):
    path = "/data/users/data-warehouse/zmtech/result/pday=%s/0*" % pday
    dest_path = "hdfs://hadoopcluster/data/production/zmtech/rpt_zmtech_yx/pday=%s" % pday
    print "rm file %s" % dest_path
    print commands.getstatusoutput("hadoop fs -rmr %s" % dest_path)
    if commands.getstatusoutput("hadoop fs -test -e %s" % dest_path)[0] != 0:
        ret = commands.getstatusoutput("hadoop fs -mkdir -p %s" % dest_path)
        print "mkdir %s" % dest_path
        print ret

    return commands.getstatusoutput("hadoop fs -put %s %s " % (path, dest_path))

def get_ftp_file(pday):
    year = pday[:4]
    month = pday[4:6]
    day = pday[6:]
    new_pday = "%s-%s-%s" % (year, month, day)
    ftp_file = "%s.tar.gz" % new_pday
    base_path = "/data/users/data-warehouse/zmtech/tmp"
    local_file = "%s/%s" % (base_path, ftp_file)

    print "get remote file ..."
    while True:
        ret = DownloadFile(ftp_file, local_file)
        if ret == 0:
            print "download file successfully ...."
            break

    print "extract file ..."

    ret = commands.getstatusoutput("tar -xvf %s -C %s" % (local_file, base_path))
    print ret

    loop_time = 0
    while True:
        extract_file = "%s/%s/*" % (base_path, new_pday)
        dest_path = "hdfs://hadoopcluster/data/production/zmtech/rawdata/pday=%s" % (pday)
        print "upload log file ..."
        print commands.getstatusoutput("hadoop fs -rmr %s" % dest_path)
        print commands.getstatusoutput("hadoop fs -mkdir -p %s" % dest_path)
        mv_path = "hadoop fs -put %s %s " % (extract_file, dest_path)
        ret = commands.getstatusoutput(mv_path)
        if ret[0] == 0:
            print "put file to hdfs successfully..."
            break
        loop_time += 1

    print "loop_time=%s " % loop_time

    remove_extract_file = "\\rm -rf %s" % extract_file
    print "remove tmp file : %s" % remove_extract_file
    print commands.getstatusoutput(remove_extract_file)
    add_partition = "hive -e \"use zmtech; msck repair table zmtech_log; \""
    print commands.getstatusoutput(add_partition)


def getDate(pastdays=7):
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=pastdays)
    yesterday = yesterday.strftime("%Y%m%d")
    return yesterday

def getPastDate(date, pastdays):
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])
    orgdate = datetime.date(year, month, day)
    targetdate = orgdate - datetime.timedelta(days=pastdays)
    targetdate = targetdate.strftime("%Y%m%d")
    return targetdate

if __name__ == '__main__':
    from optparse import OptionParser
    usage = 'usage: zmtech_rpc_client.py -d date'
    parser = OptionParser(usage=usage, version="%ZmTech 1.0")
    parser.add_option('-d', '--date', dest='date',
                      default=getDate(1), help="date")

    (options, args) = parser.parse_args()

    pday=options.date
    p30day=getPastDate(pday, 30)
    print "pday=%s, p30day=%s" % (pday, p30day)

    #get_ftp_file(pday)

    data_prepare = "set mapred.job.queue.name=mapreduce.normal;set mapred.reduce.tasks=30;" \
                   "insert overwrite table zmtech.rpt_zmtech_mac_group_uv partition(pday=%s) " \
                   " select group,upper(regexp_replace(regexp_replace(mac,':',''), '-', ''))  as mac," \
                   "count(*) as uv from zmtech.zmtech_log where pday=%s group by group,mac;" % (pday, pday)

    data_prepare_sql = "hive -e\"%s\"" % data_prepare

    print "data prepare ..."
    print data_prepare_sql
    #print commands.getstatusoutput(data_prepare_sql)

    #clean local path
    print "clean local path ..."
    source_path = "/data/users/data-warehouse/zmtech/source/pday=%s" % pday
    result_path = "/data/users/data-warehouse/zmtech/result/pday=%s" % pday
    print "clean source path : %s" % source_path
    print commands.getstatusoutput("\\rm -rf %s" % source_path)
    print "clean result path : %s" % result_path
    print commands.getstatusoutput("\\rm -rf %s" % result_path)

    path = "hdfs://hadoopcluster/data/production/zmtech/rpt_zmtech_mac_group_uv/pday=%s" % pday
    content = commands.getoutput("hadoop fs -du %s" % path)
    local_list=[]
    remote_list = []
    for line in content.split("\n"):
        file_name=line[line.rfind("/")+1:]
        if int(line.split(" ")[0]) % 3 == 0:
            local_list.append(file_name)
        else:
            #remote_list.append(file_name)
            local_list.append(file_name)

    print local_list
    print "remote_list ..."
    print remote_list

    local_list_files = "%s/{%s}" %(path, ",".join(local_list))
    print "local_list_files = %s " % local_list_files
    remote_list_files = "%s/{%s}" %(path, ",".join(remote_list))
    print "remote_list_files = %s " % remote_list_files

    # handler = ServerProxy("http://192.168.146.52:64999")
    # p = multiprocessing.Process(target = launch_task, args=(pday, remote_list_files))
    # p.start()

    l = multiprocessing.Process(target = lauch_local_task, args=(pday, local_list_files))
    l.start()

    # print "p.pid = %s" % p.pid
    print "l.pid = %s" % l.pid

    i = 0
    while True:

        time.sleep(20)
        print "loop %s times" % i
        i += 1
        #remote_status = handler.task_status(pday)
        local_status = task_status(pday)
        #if remote_status == 0 and local_status == 0:
        if local_status == 0:
            print "task finished !!!"
            break
        else:
            # print "task not finish yet: local_status=%s, remote_status=%s" % (local_status, remote_status)
            print "task not finish yet: local_status=%s " % local_status

    print "exit... "

    ret = upload_files(pday)
    print ret

    #add partition
    add_partition = "hive -e \"use zmtech;msck repair table rpt_zmtech_yx;\""
    print "add partition to ad_point.rpt_zm_tech_tmpres... "
    print commands.getstatusoutput(add_partition)

    #sqoop zhima_mapping
    sqoop_mapping = "sqoop import -D mapred.job.queue.name=mapreduce.normal  " \
                    "--connect jdbc:mysql://192.168.144.237:3306/category --username data " \
                    " --password  'PIN239!@#$%^&8' --table zhima_mapping --hive-import " \
                    "--hive-overwrite --hive-table zmtech.zhima_mapping --fields-terminated-by '\t'  -m 1 "

    print "sqoop zhima_mapping ..."
    print sqoop_mapping
    print commands.getstatusoutput(sqoop_mapping)

    #join result
    join_sql = "insert overwrite table zmtech.rpt_zmtech_base partition(pday=%s) " \
               "select a.group,c.category_id,b.mac,b.id,count(*) as uv from zmtech.rpt_zmtech_yx " \
               " b join zmtech.rpt_zmtech_mac_group_uv a  on  b.pday=%s and a.pday=%s and b.pday=a.pday and " \
               "  b.mac=a.mac join zmtech.zhima_mapping c on a.group=c.group_id " \
               " group by a.group,b.mac,b.id,c.category_id;" % (pday, pday, pday)

    join_result = "hive -e \"set mapred.job.queue.name=mapreduce.normal;%s\"" % join_sql

    print "join result ..."
    print join_result
    print commands.getstatusoutput(join_result)

    #筛选入redis的数据
    filter_sql = "insert overwrite table zmtech.rpt_zmtech_redis partition(pday=%s) select  id as pyid, unique_code, '100.0' as weight from zmtech.rpt_zmtech_base where pday<=%s and pday>%s;" % (pday, pday, p30day)
    filter_res_sql = "hive -e \"set mapred.job.queue.name=mapreduce.normal;%s\"" % filter_sql
    print "filter result ..."
    print filter_res_sql
    print commands.getstatusoutput(filter_res_sql)

    #入redis
    upload_to_redis = "sh incrementalInsert.sh hdfs://hadoopcluster/data/production/zmtech/rpt_zmtech_redis/pday=20170210/ jian.li@ipinyou.com"

    #去30天的base数据打标签
    add_tags = "insert overwrite table zmtech.rpt_zmtech_user partition(pday=%s) select id as pyid, concat_ws(',',collect_set(unique_code)) as unique_code from zmtech.rpt_zmtech_base where pday<=%s and pday > %s group by id ;" % (pday, pday, p30day)
    add_tags_sql = "hive -e \"set mapred.job.queue.name=mapreduce.normal;%s\"" % add_tags
    print "add tags ..."
    print add_tags_sql
    print commands.getstatusoutput(add_tags_sql)

