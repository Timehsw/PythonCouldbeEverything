# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/10/12.
'''

import urllib
from hashlib import md5
import hashlib
method = "GET"

host = "sspapi.gm825.net"
path = "/api_2"
apiSecret = "945471662e93b6a62222a794a080a378"
api="apiSecret="+apiSecret+"&"


reqjson = "{\"api_version\":\"2.0.0\",\"app\":{\"app_id\":\"125\",\"channel_id\":\"\",\"app_v ersion\":\"2.2.1\",\"package_name\":\"com.centurysoft.roboking.gl.wx\"},\"device\":{\"device_type\":4,\"os_type\":\"A ndroid\",\"os_version\":\"4.4.2\",\"vendor\":\"samsung\",\"model\":\"SM-G3556D\",\"android_id\":\"300b21e50c53a8b3 \",\"imei_md5\":\"24D05F85D718A511639ED5DCEEDE2AD6\",\"imei\":\"352419060231632\",\"mac\":\"14:B4:84:5A:8C:2A\",\"w\":1440,\"h\":2560},\"adslot\":{\"adslot_id\":\"44\",\"adslot_w\":1440,\"adslot_h\":800},\"network\":{\"ip\":\"192.168.0.105\",\"connect_type\":2,\"carrier\":0,\"cellular_id\":\"\"},\"gps\":{\"coordinate_type\":1,\"lon\":-1,\"lat\":-1,\" timestamp\":1447762376456}}"


req={'reqjson':reqjson}
requlicode=urllib.urlencode(req)

# print requlicode
timestamp = "1481614142971"
time="&timestamp="+timestamp


log="{method}\n{host}\n{path}\n{requlicode}{apiSecret}{time}".format(method=method,host=host,path=path,requlicode=requlicode,apiSecret=apiSecret,time=time)



m2 = hashlib.md5()
m2.update(log)
print m2.hexdigest()

