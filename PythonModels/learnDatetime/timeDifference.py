# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/4/9
"""

import datetime
from optparse import OptionParser


def defaultTime(days=0):
    return (datetime.datetime.now() + datetime.timedelta(days=days)).strftime('%Y%m%d')


def timeDifference(start, end):
    datestart = datetime.datetime.strptime(start, '%Y%m%d')
    dateend = datetime.datetime.strptime(end, '%Y%m%d')
    print '~' * 40
    print 'datestart: ', datestart.strftime('%Y%m%d')
    print 'dateend', dateend.strftime('%Y%m%d')
    print '~' * 40

    while datestart <= dateend:
        print datestart.strftime("%Y%m%d")
        datestart += datetime.timedelta(days=1)


def main():
    usage = "usage: %prog [options] starttime endtime"
    parser = OptionParser(usage=usage, version="%hsw 1.0")
    parser.add_option('-s', '--start', dest='start', type=str, default=defaultTime(),
                      help='start time!!')
    parser.add_option('-e', '--end', dest='end', type=str,
                      default=defaultTime(),
                      help='end time!!')

    (options, args) = parser.parse_args()
    timeDifference(options.start, options.end)


if __name__ == '__main__':
    main()

    # python timeDifference.py -s20170101 -e20170228
