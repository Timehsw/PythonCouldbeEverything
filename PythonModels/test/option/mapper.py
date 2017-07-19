#!/usr/bin/env python
# coding=utf-8
__author__ = 'zenith'
import sys

for line in sys.stdin:
    for word in line.strip().split():
        print("%s\t%s" % (word, 1))
