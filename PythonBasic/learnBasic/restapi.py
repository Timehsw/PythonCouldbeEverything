# coding=utf8
__author__ = 'zenith'

import httplib,json
url = "http://192.168.1.162:34343/metrics"
conn = httplib.HTTPConnection("192.168.1.162","34343")
conn.request("GET",url)
response = conn.getresponse()
res= response.read()
obj=json.loads(res)
for k,v in dict(obj).items():
    for k1,v1 in dict(v).items():
        print("pkey:%s  \t key:%s \t value:%s"%(k,k1,v1))

