# encoding=utf-8
import MySQLdb
import httplib
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class ReadMysql(object):
    def __init__(self):
        self.database = MySQLdb.connect(host="192.168.15.15", user="root", passwd="5Rb!!@bqC%", db="jusfoun_warehouse",
                                        charset="utf8")
        self.cursor = self.database.cursor()

    def get(self):

        try:
            sql = """SELECT
                    a.source_id,
                    a.uid,
                    a.source_name,
                    a.note,
                    b.hive_name,
                    c.category_id
                    FROM
                        dw_source a
                    LEFT JOIN dw_hdfs b ON a.source_id = b.source_id
                    LEFT JOIN rel_category_table c ON a.source_id = c.resource_id
                    WHERE
                        a.source_type = 4
            """
            # print sql
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            arr = []
            for row in result:
                dic = {}
                source_id = row[0]
                userId = row[1]
                showname = row[2]
                description = row[3]
                tablename = row[4]
                categoryId = row[5]
                #
                dic['source_id'] = source_id
                dic['userId'] = userId
                dic['showname'] = showname
                dic['description'] = description
                dic['tablename'] = tablename
                dic['categoryId'] = categoryId
                dic['databasename'] = 2
                # print "source_id=%s,uid=%s,source_name=%s,note=%s,hive_name=%s,category_id=%s" % (source_id, userId, showname, description, tablename, categoryId)
                self.insertdata(dic)
                # time.sleep(1)
        except Exception, e:
            print str(e)
        self.end()

    def insertdata(self, dic):
        str = ''
        for k, v in dic.items():
            tmp = "%s=%s&" % (k, v)
            str = str + tmp

        str = str[:-1]
        url = "http://192.168.15.14:8688/superset/addrecord?" + str
        print url
        conn = httplib.HTTPConnection("192.168.15.14", "8688")
        conn.request("GET", url)
        response = conn.getresponse()
        res = response.read()
        print res

    def end(self):
        self.database.commit()
        self.cursor.close()
        self.database.close()
        print "Over ... "


if __name__ == '__main__':
    mysql = ReadMysql()
    mysql.get()
