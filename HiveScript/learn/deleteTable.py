# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/8/10.
'''

import subprocess

def run_it(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True,
                         stderr=subprocess.PIPE)
    print ('running:%s' % cmd)
    out, err = p.communicate()
    if p.returncode != 0:
        print ("Non zero exit code:%s executing: %s \nerr course ---> %s" % (p.returncode, cmd, err))
    return out


def hive_command(tableName):
    command='''hive -e "use dsp;drop table %s;" ''' % tableName
    print command
    # run_it(command)


def dealTmpTable():
    commands=''
    with open('./tables.txt', 'r') as f:
        tables = f.readlines(10000000000000)
        for table in tables:
            # print "--->" + table
            command="drop table %s;" %table
            commands+=command
            # hive_command(table)
    print commands


commands=dealTmpTable()
print commands