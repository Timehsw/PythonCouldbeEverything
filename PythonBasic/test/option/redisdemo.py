# -*- coding: utf-8 -*-
"""
Created by hushiwei on 16-12-27.
"""

import redis

pool = redis.ConnectionPool(host='192.168.15.13', port=6379)
r = redis.Redis(connection_pool=pool)
# print r.hget('pt_session_user058256f4081a43b38a8efbec236f4142','id')
# print r.hgetall('pt_session_user058256f4081a43b38a8efbec236f4142')
# print r.hgetall('pt_session_user058256f4081a43b38a8efbec22222')
print r.hgetall('pt_session_user7bc7104ab607469fa0e6a130fcf0c8de')
# print r.hgetall('pt_session_useraaca647c6b714efaab64e3e8b89957ee')

# r.hmset('pt_session_user058256f4081a43b38a8efbec236f4142',{'username':'hushiwei'})
# r.hmset('pt_session_user058256f4081a43b38a8efbec22222',{'id':'110'})