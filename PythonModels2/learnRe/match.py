# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/7/20
"""

import re

pattern = re.compile("\d+")

# match从字符串开头开始查找,字符串开头是字符，不是数字，因此匹配不到
# matcher=pattern.match("aaa123vvvvv6768")

matcher = pattern.match("aaa123vvvvv6768", 3, 5)

print matcher.group()


pattern1=re.compile(r"([a-z]+) ([a-z]+)",re.I)

matcher1=pattern1.match("Hello World Spark Hadoop")

print matcher1.group(0) # group(0)代表匹配的所有子串
print matcher1.group(1) # group(1)代表匹配的第一个子串
print matcher1.group(2) # group(2)代表匹配的第二个子串
