# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/5/2
"""
import subprocess
import datetime
import argparse
import csv
import gzip
import happybase
import logging

def connect_to_hbase():
    return happybase.Connection('10.10.25.217',autoconnect=False)

def main():
    logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s: %(message)s',level=logging.INFO)

    argp = argparse.ArgumentParser(description='EventLog Reader')
    argp.add_argument('-t','--table', dest='table', default='eventlog')
    argp.add_argument('-p','--prefix', dest='prefix')
    argp.add_argument('-f','--filter', dest='filter')
    argp.add_argument('-l','--limit', dest='limit', default=10)

    args = argp.parse_args()

    hbase_conn = connect_to_hbase()
    hbase_conn.open()

    # print 所有表名

    hbaseTables=hbase_conn.tables()
    for tablename in hbaseTables:
        print tablename


if __name__ == '__main__':
    main()
