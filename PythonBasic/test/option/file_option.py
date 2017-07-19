# coding=utf-8
__author__ = 'zenith'

"""中文"""

import chardet

data = open('D:\\data.txt', 'r')
"""

text= data.read()
print(text)
print chardet.detect(text)

print(chardet.detect(text.decode("gbk").encode("gbk")))

data.close()


data_write = open('D:\\data.txt', 'w')
data_write.write('hello你好\n在吗？'.decode('utf-8').encode('gbk'))
data_write.close()


"""
data_append = open('D:\\data.txt', 'a')
data_append.write('hello你好\n在吗？')
data_append.close()
