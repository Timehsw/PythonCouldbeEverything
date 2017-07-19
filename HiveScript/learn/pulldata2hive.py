# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/3/28
"""

import os, sys
reload(sys); sys.setdefaultencoding( "utf-8" )
flag_server = int(os.popen('ifconfig | grep "inet addr:172" | wc -l').read().strip())
dir_scripts = '/app/home/zhangb/' if flag_server else '/Users/zhangb/Desktop/'
dir_data = '/app/home/zhangbo/' if flag_server else '/Users/zhangb/Desktop/'
dir_server = '/app/home/'
sys.path.append(dir_scripts)

import datetime
import time
db_name = 'zhangb'

def hive_day_cid(create_date,type11_duration):
    #原始表geohash表关联，找到cid
    # ------------------   建立 geohash 表   -------------------- #
    print "# ---------------------------------------------------------------------------------- #"

    start_date_str = (create_date - datetime.timedelta(days=type11_duration-1)).strftime("%Y%m%d")
    end_date_str   = create_date.strftime("%Y%m%d")

    hive_command = ( '''
hive -e " use %s;
    create table if not exists hive_day_cid_provider(provider string,day int, cnt_cid bigint,dist_cid bigint );

    insert into hive_day_cid_provider
    select a.provider,a.day,count(a.cid) as cnt_cid,count(distinct(a.cid)) as dist_cid from
    (select day,provider,token_md5 as cid  from  report_ods_mdp.upload_bi_type11
    where day >=%s and day <= %s  and length(token_md5)>0 and provider in ('gps','network','passive','none') ) a
    group by a.provider,a.day

;"
    ''' % ( db_name,start_date_str, end_date_str) )

    print hive_command
    if flag_server:
        os.system(hive_command)
    print "\n"




if __name__ == '__main__':

    start = time.time()
    business_name = 'brand48'
    # ----------------------------------------
    #7号是这个周期中的最后一天，是周期结束日期
    for (i,j) in [ (11,7),(11,14),(11,28),(12,5),(12,12),(12,19),(12,26)]:
        # for (i, j) in [(2, 7), (2, 14), (2, 21), (2, 28)]:
        create_date = datetime.date(2016,i,j)
        type11_duration=7
        hive_day_cid(create_date,type11_duration)
        print "\r"
        print '# Time: ', str(datetime.timedelta(seconds=(time.time() - start)))
        print '# the end'
        print '\n'

    #hive_imei_time_list(create_date,type11_duration)
    print '# Time: ', str(datetime.timedelta(seconds=(time.time() - start)))

    # Beintoo_day.hive_output(create_date, cnt_duration=7)
'''
for i in range(1,30):
    a=datetime.date(2016, 2, 23)
    b=a+ datetime.timedelta(7*i)
    print b
'''
#===跨年的时候处理方法1
'''
date_begin = datetime.date(2016,12,1)
    # date_end = date_begin
    date_end = datetime.date(2017,1,10)
    for i in range(0,(date_end - date_begin).days+1,7):
        create_date = date_begin + datetime.timedelta(days=i)

        print create_date

#方法2
date_begin = datetime.date(2016,12,1)
    # date_end = date_begin
    date_end = datetime.date(2017,1,10)

 while date_begin <= date_end:
        print date_begin
        date_begin = date_begin + datetime.timedelta(days=7)
'''