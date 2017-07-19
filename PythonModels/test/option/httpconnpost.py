# coding=utf-8
__author__ = 'zenith'

import urllib
import httplib

test_data = {'name': 'A',
             'note': '',
             'pageNum': 1,
             'pageSize': 15
             }
test_data_urlencode = urllib.urlencode(test_data)
requrl = "http://data.galaxybigdata.com/warehouse/warehouse/source/list"
headerdata = {"Host": "data.galaxybigdata.com"}
conn = httplib.HTTPConnection("data.galaxybigdata.com")
conn.request(method="POST", url=requrl, body=test_data_urlencode, headers=headerdata)
response = conn.getresponse()
res = response.read()
print res
conn.close()
