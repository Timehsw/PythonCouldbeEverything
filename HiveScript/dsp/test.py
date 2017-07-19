# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/4/18
"""

sqoop_mapping = "sqoop import -D mapred.job.queue.name=mapreduce.normal  " \
                "--connect jdbc:mysql://192.168.144.237:3306/category --username data " \
                " --password  'PIN239!@#$%^&8' --table zhima_mapping --hive-import " \
                "--hive-overwrite --hive-table zmtech.zhima_mapping --fields-terminated-by '\t'  -m 1 "


print sqoop_mapping