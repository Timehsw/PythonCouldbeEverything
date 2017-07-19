# -*- coding: utf-8 -*-
"""
Created by hushiwei on 16-12-24.
"""
import os
import shutil
import codecs

from jinja2 import Environment, FileSystemLoader
import pypinyin

# 静态文件路径，默认为`/static/`
# 表示使用flask发布网站时的`http://ip:port/static/`目录
# 也可指定为固定地址的静态文件url，例如："http://192.168.62.47:5000/static/"
# 注意，使用其他域名的静态文件时有可能引起跨域问题
STATIC_ROOT = "/static/"

# Markdown文件读取目录
INPUT_CONTENT = "../in/"

# 索引文件
INDEX_DAT = "../static/out/index.dat"

# html生成输出目录
OUTPUT_CONTENT = "../static/out/"

env = Environment(
    loader=FileSystemLoader("templates")
)


# 标签倒排索引
TAG_INVERTED_INDEX = {}
# 作者倒排索引
AUTHOR_INVERTED_INDEX = {}

# 文章索引
ARTICLE_INDEX = {}

_MD_FILES = []

_current_file_index = None
_pinyin_names = set()

TAG_HTML_TEMPLATE = u"<a href='/tag/{tag}/' class='tag-index'>{tag}</a>"
AUTHOR_HTML_TEMPLATE = u"<a href='' class='tag-index'>{author}</a>"
TITLE_HTML_TEMPLATE = u"<div class='sidebar-module-inset'><h5 class='sidebar-title'><i class='icon-circle-blank side-icon'></i>标题</h5><p>{title_str}</p></div>"

def _reload_global():
    global TAG_HTML_TEMPLATE,AUTHOR_HTML_TEMPLATE,TITLE_HTML_TEMPLATE,\
        _MD_FILES,_current_file_index,_pinyin_names

    TAG_INVERTED_INDEX = {}
    AUTHOR_INVERTED_INDEX = {}
    ARTICLE_INDEX = {}
    _MD_FILES = []
    _current_file_index = None
    _pinyin_names = set()

def clean():
    '''
    清理输出文件夹
    '''
    if os.path.exists(OUTPUT_CONTENT):
        shutil.rmtree(OUTPUT_CONTENT)

def load_md_files(folder):
    '''从指定位置载入markdown文件
    '''
    global _MD_FILES
    for root,dirs,files in os.walk(folder):
        for f in files:
            if os.path.splitext(f)[1].lower()==".md":
                _MD_FILES.append(os.path.join(root,f))

def str2pinyin(hans,style=pypinyin.FIRST_LETTER):
    '''字符串转拼音，默认只获取首字母
    '''
    pinyin_str=pypinyin.slug(hans,style=style,separator="")
    print "-->",pinyin_str
    num=2
    while pinyin_str in _pinyin_names:
        pinyin_str+=str(num)
        num+=1
    return pinyin_str

def get_out_dir(md_file):
    '''获取md文件的输出路径
    '''
    return os.path.join(OUTPUT_CONTENT,_current_file_index+".html")
def gen(md_file_path):
    '''md生成html文件'''
    get_out_dir(md_file_path)



def scan_md():
    '''扫描 md文件'''
    global _current_file_index
    for f in _MD_FILES:
        file_base_name=os.path.splitext(os.path.basename(f))[0]
        _current_file_index=str2pinyin(
            codecs.decode(file_base_name,"gb2312")
        )
        print _current_file_index
        _pinyin_names.add(_current_file_index)
        gen(f)
def generate():
    _reload_global()
    clean()

    load_md_files(INPUT_CONTENT)
    scan_md()



    # pass


if __name__ == '__main__':
    generate()