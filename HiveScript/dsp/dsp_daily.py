# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/4/17
"""

import subprocess
import datetime
from optparse import OptionParser

WORKROOT = ""


def defaultTime(days=1):
    return (datetime.datetime.now() - datetime.timedelta(days=days)).strftime('%Y%m%d')


def defaultHour():
    return datetime.datetime.now().strftime('%H')


def run_it(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True,
                         stderr=subprocess.PIPE)
    print ('running:%s' % cmd)
    out, err = p.communicate()
    if p.returncode != 0:
        print ("Non zero exit code:%s executing: %s \nerr course ---> %s" % (p.returncode, cmd, err))
    return out


def main():
    usage = "usage: %prog [options] date hour"
    parser = OptionParser(usage=usage, version="%hsw 1.0")
    parser.add_option('-d', '--date', dest='date', type=str, default=defaultTime(),
                      help='yesterday time!!')
    parser.add_option('-t', '--hour', dest='hour', type=str,
                      default=defaultHour(),
                      help='hour!!')

    (options, args) = parser.parse_args()

    yesteday = options.date
    hour = options.hour
    ooziecmd = "oozie job -oozie http://${OOZIE_SERVER}:11000/oozie/" \
                "-config %s/wf/job.properties" \
                "-run -verbose -Dday=%s -Dhour=%s" % (WORKROOT, yesteday, hour)

    print ooziecmd


if __name__ == '__main__':
    main()
