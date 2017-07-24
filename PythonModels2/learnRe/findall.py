# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/7/20
"""

import re

pattern=re.compile(r"\d+")

m=pattern.findall("hello 123 45")

print m