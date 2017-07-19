# coding=utf8
__author__ = 'zenith'
import MySQLdb
#db = MySQLdb.connect("127.0.0.1","root","123456","myciti" )
# db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="haha", db="test",charset="utf8")
# db_cursor=db.cursor()
# sql="insert into t_user(name,address,phone) VALUEs('%s','%s','%s')"%('crxy','crxy','111111')
# db_cursor.execute(sql)
# db.commit()
# db.close()

# opt['url']='jdbc:mysql://192.168.4.213:3306/lex'
# opt['driver']='com.mysql.jdbc.Driver'
# opt['dbtable']='company1'
# opt['user']='root'
# opt['password']='5Rb!!@bqC%'

db = MySQLdb.connect(host="192.168.15.15", user="root", passwd="5Rb!!@bqC%", db="sparkSQL",charset="utf8")
db_cursor=db.cursor()
sql="select * from CSDNSpark"
db_cursor.execute(sql)
#result=db_cursor.fetchall()
result=db_cursor.fetchone()
print(result)
# print(db_cursor.fetchone())
# print(db_cursor.fetchone())
# print(db_cursor.fetchone())
# for re in result:
#  print(isinstance(re[1],unicode))

db.close()

