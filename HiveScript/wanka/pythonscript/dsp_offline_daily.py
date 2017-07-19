# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/4/17
"""

import subprocess
import datetime
import time
from optparse import OptionParser
import ConfigParser
import os

confPath = os.path.join(os.path.dirname(os.getcwd()),
                        "conf/ApplicationEnv.ini")


def readConfig(file="config.ini"):
  """ 把应用相关的参数存储到字典中"""
  app = {}
  streaming = {}
  config = ConfigParser.ConfigParser()
  config.read(file)
  apps = config.items("APPLICATION")
  paras = config.items("Streaming")
  for arg in apps:
    app[arg[0]] = arg[1]
  for ays in paras:
    streaming[ays[0]] = ays[1]
  return app, streaming


def defaultTime(days=1):
  return (datetime.datetime.now() - datetime.timedelta(days=days)).strftime(
      '%Y%m%d')


def defaultHour():
  return 23


def defaultCTime():
  return int(time.time())


def run_it(cmd):
  p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True,
                       stderr=subprocess.PIPE)
  print ('running:%s' % cmd)
  out, err = p.communicate()
  if p.returncode != 0:
    print ("Non zero exit code:%s executing: %s \nerr course ---> %s" % (
      p.returncode, cmd, err))
  return out


# 执行日常任务
def exec_daily(yesterday, hour, ctime):
  app, streaming = readConfig(confPath)
  ooziecmd = "oozie job -oozie http://%s:11000/oozie/ " \
             "-config %s/wf/job.properties " \
             "-run -verbose -Dday=%s -Dhour=%s -Dtime=%s" % (
               app['oozie_server'], app['workroot'], yesterday, hour, ctime)

  # out = run_it(ooziecmd)
  # print out
  print ooziecmd


# 执行小时任务
def exec_hour(yesterday, hour):
  app, streaming = readConfig(confPath)
  ooziecmd = "oozie job -oozie http://%s:11000/oozie/ " \
             "-config %s/hourwf/job.properties " \
             "-run -verbose -Dday=%s -Dhour=%s" % (
               app['oozie_server'], app['workroot'], yesterday, hour)
  print ooziecmd


# 执行地域定向任务
def exec_areacode(yesterday, hour, ctime):
  app, streaming = readConfig(confPath)
  ooziecmd = "oozie job -oozie http://%s:11000/oozie/ " \
             "-config %s/targetingwf/job.properties " \
             "-run -verbose -Dday=%s -Dhour=%s -Dtime=%s" % (
               app['oozie_server'], app['workroot'], yesterday, hour, ctime)
  print ooziecmd


def pullDataFromRemote(day, hour, isHour=0):
  app, streaming = readConfig(confPath)
  logpath = "%s/source_log/%s" % (app['workroot'], day)
  logDirname = datetime.datetime.strptime(day, "%Y%m%d").strftime("%y_%m_%d")
  # 判断按照天还是小时统计，按照天统计，logname例如：15_08_09.log 按照小时统，logname例如：15_08_09_03.log
  logFilePath = "%s/%s.log" % (logpath, logDirname)
  if isHour is 0:
    if os.path.exists(logFilePath) is False:
      # os.remove(logFilePath)
      for i in range(24):
        j = i
        if i < 10:
          j = "0%s" % str(i)
        logname = "%s_%s.log" % (logDirname, j)
        getLogsByHour(day, logname)

  # 删除历史日志
  target_day=(datetime.datetime.strptime(day, "%Y%m%d")-datetime.timedelta(2)).strftime('%Y%m%d')
  print "%s/source_log/%s" % (app['workroot'],target_day)
  if os.path.isdir("%s/source_log/%s" % (app['workroot'],target_day)):
    os.removedirs("%s/source_log/%s" % (app['workroot'],target_day))






def getLogsByHour(day, logname):
  nyr=datetime.datetime.strptime(logname[0:8], "%y_%m_%d").strftime("%Y%m%d")
  app, streaming = readConfig(confPath)
  logpath = "%s/source_log/%s" % (app['workroot'], day)
  logFilePath = "%s/%s" % (logpath, logname)
  resultPath="%s/%s.log" % (logpath, nyr)
  # print logFilePath
  reqHosts = app['request_log_host'].split(",")
  if os.path.exists(logFilePath):
    os.remove(logFilePath)
  for reqHost in reqHosts:

    cmdimp="scp -o GSSAPIAuthentication=no {ssh_user}@{reqHost}:{dspAppRoot}/{logname}* " \
    "{logFilePath}_bak".format(ssh_user=app['ssh_user'],reqHost=reqHost,dspAppRoot=app['dsp_app_promotion_implog'],logname=logname,logFilePath=logFilePath)
    print cmdimp
    cmddwnl="scp -o GSSAPIAuthentication=no {ssh_user}@{reqHost}:{dspAppRoot}/{logname}* " \
           "{logFilePath}_bakdwnl".format(ssh_user=app['ssh_user'],reqHost=reqHost,dspAppRoot=app['dsp_app_promotion_dwnllog'],logname=logname,logFilePath=logFilePath)
    print cmddwnl
    run_it(cmddwnl)

    if os.path.exists("%s_bak"%logFilePath):
      mergeCmd="cat %s_bak >> %s" % (logFilePath,resultPath)
      print mergeCmd
      os.remove("%s_bak"%logFilePath)
    if os.path.exists("%s_bakdwnl"%logFilePath):
      mergeCmd="cat %s_bakdwnl >> %s" % (logFilePath,resultPath)
      print mergeCmd
      os.remove("%s_bakdwnl"%resultPath)


def main():
  usage = "usage: %prog [options] date hour"
  parser = OptionParser(usage=usage, version="%hsw 1.0")
  parser.add_option('-d', '--date', dest='date', type=str,
                    default=defaultTime(),
                    help='yesterday time!!!')
  parser.add_option('-t', '--hour', dest='hour', type=str,
                    default=defaultHour(),
                    help='hour!!!')
  parser.add_option('-s', '--ctime', dest='ctime', type=str,
                    default=defaultCTime(),
                    help='currentTime!!!')

  (options, args) = parser.parse_args()

  yesterday = options.date
  hour = options.hour
  ctime = options.ctime
  app, streaming = readConfig(confPath)
  #  新建存储拉取日志的目录
  logpath = "%s/source_log/%s" % (app['workroot'], yesterday)
  if os.path.isdir(logpath) is not True:
    os.makedirs(logpath)
    # print logpath
  #  数据采集,上传到 HDFS
  pullDataFromRemote(yesterday, hour)


if __name__ == '__main__':
  main()
