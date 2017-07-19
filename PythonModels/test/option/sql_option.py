# coding=utf-8
__author__ = 'zenith'
import MySQLdb

"""
try:

    #db = MySQLdb.connect("192.168.1.155", "root", "haha", "test")
    db = MySQLdb.connect(host="192.168.1.155", user="root", passwd="haha", db="test",charset="utf8")
    db_add = db.cursor()

    #sql = "insert into t_user(name,address,phone) values ('%s','%s','%s');" % ('zenith', '南京', '12233344566');
    sql = "update t_user set address='new 上海' where name='zenith'";
    print(db_add.execute(sql))

    db.commit()
except Exception as ex:
    print(ex.message)
    db.rollback()

finally:
    db.close()





"""
db = MySQLdb.connect(host="192.168.1.155", user="root", passwd="haha", db="test",charset="utf8")
db_get = db.cursor()

sql = "select * from t_user";
db_get.execute(sql)
data=db_get.fetchall()

for i in data:
    print(i[2].encode("utf-8"))
db.close()

