# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/7/20
"""

import re

pattern = re.compile(r"\d+")

# search是从任意位置开始匹配的，所以这次就可以匹配到内容，match是从开始匹配的，所以匹配不到内容
m = pattern.search(r"aaa123dddf4645")
# m = pattern.match(r"aaa123dddf4645")

print m.group()

m1=pattern.search("vvv2345 456")

print m1.group()