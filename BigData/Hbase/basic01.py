# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/5/2
"""

import happybase

connection=happybase.Connection('10.10.25.217',autoconnect=False)
connection.open()

# print 所有表名
print ('All tables: ',connection.tables(), '\n')


#操作testtable表
#这个操作是一个提前声明-我要用到这个表了-但不会提交给thrift server做操作
table = connection.table(b'dmp_wanka2')

#检索某一行
row = table.row(b'000a00f299353d48043dac75251d2709')
print('a row:', row, '\n')

#right
print(row[b'app:applist'])
print(row[b'info:channel_id'])
print(row[b'info:ct'])

#wrong
# print(row['app:applist'])
# print(row['info:channel_id'])
#
#显示所有列族
print'所有列族', table.families(), '\n'


#输出两列
print('print two rows:')
rows = table.rows([b'000e1a4639b6522977d7ae037323158e', b'000eca6a95c063e35342a12c9acb4435'])
for key, data in rows:
	print(key, data)

#字典输出两列
print '\n'+'print two dict rows'
rows_as_dict = dict(table.rows([b'000e1a4639b6522977d7ae037323158e', b'000eca6a95c063e35342a12c9acb4435']))
print(rows_as_dict)

#输入row的一个列族所有值
row = table.row(b'000e1a4639b6522977d7ae037323158e', columns=[b'info'])
print '\n','输出一个列族',row

#scan操作
# print '\n', 'do scan'
# for key, data in table.scan():
# 	print(key, data)