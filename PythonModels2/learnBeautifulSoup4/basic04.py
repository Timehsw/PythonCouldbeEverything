# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/23.
'''

'''
遍历文档树
'''
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 创建beautifulsoup对象
soup = BeautifulSoup(html, "lxml")

for item in soup.html.contents:
    print item

print '~'*50

for child in soup.descendants:
    print child

print '~'*50

arr= soup.body.contents
for item in arr:
    print item

print '~'*50
for child in  soup.body.children:
    print child
