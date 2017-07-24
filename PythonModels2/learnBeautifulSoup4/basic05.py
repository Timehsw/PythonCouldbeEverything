# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/23.
'''

'''
搜索文档树
find_all(name, attrs, recursive, text, **kwargs)

name 参数
name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉

select
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

for tag in  soup.find_all("a"):
    print tag

print '`'*80

print soup.find_all(id="link2")[0].string
print soup.find_all(attrs={"class":"sister"})[0].string

print '`'*80

# 通过标签名查找
print soup.select('title')
print soup.select('p')

print '`'*80
# 通过类名查找
print soup.select(".sister")

print '`'*80
# 通过id查找
print soup.select("#link2")

# 组合查找
'''
组合查找即和写 class 文件时，标签名与类名、id名进行的组合原理是一样的，例如查找 p 标签中，id 等于 link1的内容，二者需要用空格分开
'''