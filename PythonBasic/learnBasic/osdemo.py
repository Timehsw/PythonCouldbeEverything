import os
basedir = os.path.abspath(os.path.dirname(__file__))
print basedir
path=os.path.dirname(__file__)
print path

DATA_DIR = os.path.join(os.path.expanduser('~'), '.superset')
print DATA_DIR

l=os.path.expanduser('~')
print l

en=os.environ
for k in en.keys():
    print "%s  ---  %s" % (k,en[k])
#
# get current path, try to use PWD env first
# import sys
# arr=['a','b']
# arr.insert(0, sys.executable)
#
# print arr
# ['/usr/bin/python2.7', 'a', 'b']
aa=os.environ.get('MAIL_USERNAME')
print aa