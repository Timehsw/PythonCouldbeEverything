# coding=utf-8
__author__ = 'zenith'

import httplib,json
url = "http://192.168.15.14:8688/superset/addrecord?description=None&userId=123&tablename=0ccd89dddb45&databasename=2&source_id=1001974590672622370760&categoryId=1&showname=天津市著名商标查询"
# url = "http://data.galaxybigdata.com/warehouse/warehouse/label/all"
conn = httplib.HTTPConnection("192.168.15.14","8688")
# conn = httplib.HTTPConnection("data.galaxybigdata.com")
conn.request("GET",url)
response = conn.getresponse()
res= response.read()
# obj=json.loads(res)

# print obj.get("CHANNEL.c1").get("EventTakeSuccessCount"),obj.get("CHANNEL.c1").get("EventPutAttemptCount")
print res

