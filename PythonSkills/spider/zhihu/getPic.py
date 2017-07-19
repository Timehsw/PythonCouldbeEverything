# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/5/8
"""

import requests
from lxml import html
import os
# 编码问题，可以加下面三行
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
	'Cookie': 'd_c0="ACCCItg0bguPTuSWzkKoBlPEFSv_VHbV4f4=|1489154388"; _zap=a1cd94b2-4f86-4883-917b-3915b8cb26e9; q_c1=2343456a6f4546169eff16afd3ca3eda|1491820993000|1489154388000; r_cap_id="OTYxNzI2NWE4ZmFiNGI5N2FiMDVkMzM0ZmQ2NTIxNjU=|1493197306|99984250e536fd594aef0d27059c23fa9b2b1dfd"; cap_id="N2NlZjE2ZmM3MzM1NDVlNjkzODFjYjNhYTU1NDk4YjY=|1493197306|0076e5031a447c4b2706d3e7ddc52a3d1fed3b5e"; aliyungf_tc=AQAAAMPGhhSq4ggAaeD4coNuQelyHxBZ; acw_tc=AQAAAFv0vjINngkAaeD4citaIsXeJ/Lk; _xsrf=49eda927596c7851897cf63708e369a2; __utmt=1; z_c0=Mi4wQUFDQWViRWNBQUFBSUlJaTJEUnVDeGNBQUFCaEFsVk5DZThuV1FDa2R5bHN5YUFZcHNXZnZzU24wT09LMlF6Vml3|1494229081|45b7c6e2a515b44f8e890ee8c77a2348d07d623c; __utma=51854390.923740731.1493197311.1493197311.1494229034.2; __utmb=51854390.5.9.1494229162828; __utmc=51854390; __utmz=51854390.1493197311.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100-1|2=registration_date=20130729=1^3=entry_date=20130729=1'
}


def get_link_ist(collection_num):
	page = input('你想要多少页？(注意身体哦～):')
	result = []
	collection_title = None
	for i in range(1, page+1):
		link = 'https://www.zhihu.com/collection/{}?page={}'.format(collection_num, i)
		response = requests.get(link, headers=headers).content
		sel = html.fromstring(response)
		# 创建文件夹
		if collection_title is None:
			# 收藏夹名字
			collection_title = sel.xpath('//h2[@class="zm-item-title zm-editable-content"]/text()')[0].strip()
			if not os.path.exists(collection_title):
				os.mkdir(collection_title)
		each = sel.xpath('//div[@class="zm-item"]//div[@class="zm-item-answer "]/link')
		for e in each:
			link = 'https://www.zhihu.com' + e.xpath('@href')[0]
			result.append(link)
	return [collection_title, result]


def get_pic(collection, answer_link):
	response = requests.get(answer_link, headers=headers).content
	sel = html.fromstring(response)
	title = sel.xpath('//h1[@class="QuestionHeader-title"]/text()')[0].strip()
	try:
		# 匿名用户
		author = sel.xpath('//a[@class="UserLink-link"]/text()')[0].strip()
	except:
		author = u'匿名用户'
	# 新建路径
	path = collection + '/' + title + ' - ' + author
	try:
		if not os.path.exists(path):
			os.mkdir(path)
		n = 1
		for i in sel.xpath('//div[@class="RichContent-inner"]//img/@src'):
			# 去除whitedot链接
			if 'whitedot' not in i:
				# print i
				pic = requests.get(i).content
				fname = path + '/' + str(n) + '.jpg'
				with open(fname, 'wb') as p:
					p.write(pic)
				n += 1
		print u'{} 已完成'.format(title)
	except :
		pass


if __name__ == '__main__':
	collection_num = input('输入收藏夹号码：')
	r = get_link_ist(collection_num)
	collection = r[0]
	collection_list = r[1]
	for k in collection_list:
		get_pic(collection, k)