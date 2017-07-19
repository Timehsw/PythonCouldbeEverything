# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/5/16
"""
import sys
if __name__ == '__main__':
	if len(sys.argv) >= 2:
		if sys.argv[1] == 'upgradedb':
			# 更新数据库结构，初次获取或更新版本后调用一次python main.py upgradedb即可
			print "hello"
			print sys.argv[0]
			exit(0)

	print "------------"