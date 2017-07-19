#!/usr/bin/env python
# coding=utf-8
__author__ = 'zenith'

import sys

current_word=None
current_count=0

for line in sys.stdin:
    world,count=line.strip().split('\t',1)
    try:
        count=int(count)
    except ValueError:
        continue
    if world==current_word:
        current_count+=count
    else:
        if current_word:
            print("%s\t%s"%(current_word,current_count))
        current_word=world
        current_count=count
if current_word:
    print("%s\t%s"%(current_word,current_count))


