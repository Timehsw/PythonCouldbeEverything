# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/19.
'''

'''
什么时候用urllib?什么时候用urllib2呢?
1.urllib没有Response对象,无法传入header等信息.
2.所以创建请求都是用urllib2
3.urllib模块中有一个urlencode方法,可以编码中文作为参数.但是urllib2中没有这个方法
4.这些就是为什么urllib和urllib2总是在一起用的一些原因

一般HTTP请求提交数据，需要编码成 URL编码格式，然后做为url的一部分，或者作为参数传到Request对象中。
'''
import urllib

keyword='三国演义'

word={"wd":keyword}

# 编码
search_word=urllib.urlencode(word)
# wd=%E4%B8%89%E5%9B%BD%E6%BC%94%E4%B9%89
print search_word

# 解码
print urllib.unquote(search_word)
# wd=三国演义