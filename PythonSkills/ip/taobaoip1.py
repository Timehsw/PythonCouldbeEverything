# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/11/10.
    alfred以前只支持xml格式返回
'''

import urllib2
import json
from xml.etree.ElementTree import Element, SubElement
from xml.etree import ElementTree
from xml.dom import minidom
import hashlib
import sys

def generate_feedback(ip, title, subtitle):
    items = Element('items')
    uid = hashlib.md5(ip).hexdigest()
    arg = title
    item = SubElement(items, 'item', {'uid': uid, 'arg': arg})
    element_item_title = SubElement(item, 'title')
    element_item_title.text = title
    element_item_subtitle = SubElement(item, 'subtitle')
    element_item_subtitle.text = subtitle
    element_item_icon = SubElement(item, 'icon')
    element_item_icon.text = "icon.png"

    rough_string = ElementTree.tostring(items, 'utf-8')
    print rough_string
    #print minidom.parseString(rough_string).toprettyxml(indent="    ")

ip = u'{query}'
#ip = sys.argv[1]
ip_taobao_api_url = "http://ip.taobao.com/service/getIpInfo.php?ip="

f = urllib2.urlopen(ip_taobao_api_url + ip)
#print f.read()

result = json.loads(f.read())
# return code: 0: success, 1: failed
#code result["code"]
area = result["data"]["area"]
city = result["data"]["city"]
country = result["data"]["country"]
isp = result["data"]["isp"]
region = result["data"]["region"]

title = "%s %s %s" % (country, region, city)
subtitle = "%s %s" % (area, isp)

generate_feedback(ip, title, subtitle)
