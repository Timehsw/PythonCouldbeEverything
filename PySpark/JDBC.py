# coding:utf-8
'''
    Created on 2016/7/19 0019
    @Author:   HuShiwei
'''

'''
执行命令 spark-submit --packages mysql:mysql-connector-java:5.1.39 JDBC.py   成了
'''

from PySpark import SparkConf, SparkContext
from PySpark.sql import SQLContext
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
# os.environ["SPARK_HOME"] = "/usr/hdp/2.4.0.0-169/spark"
os.environ["SPARK_HOME"] = "/opt/spark"


def save(tablename):
    conf = SparkConf().setAppName("python model").setMaster("local[*]")
    sc = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)

    hostname = "10.23.73.118"
    dbname = 'ouye'
    jdbcPort = '3306'
    properties = {
        "user": 'root',
        "password": 'jusfoun@123',
        "driver": 'com.mysql.jdbc.Driver'
    }
    jdbcUrl = "jdbc:mysql://{0}:{1}/{2}?characterEncoding=utf8".format(hostname, jdbcPort, dbname)

    df = sqlContext.read.jdbc(url=jdbcUrl, table=tablename, properties=properties)

    df.show()

    # df.write.parquet("hdfs://Jusfoun2016/hsw/out67")


if __name__ == '__main__':
    save(sys.argv[1])
