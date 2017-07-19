# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/3/28
"""

''''
1.首先，必须 import OptionParser 类，创建一个 OptionParser 对象：
2.然后，使用 add_option 来定义命令行参数：
3.每个命令行参数就是由参数名字符串和参数属性组成的。如 -f 或者 –file 分别是长短参数名：
4.最后，一旦你已经定义好了所有的命令行参数，调用 parse_args() 来解析程序的命令行：

解释:
parse_args() 返回的两个值：
options，它是一个对象（optpars.Values），保存有命令行参数值。只要知道命令行参数名，如 user，就可以访问其对应的值： options.user

action有三种类型：
    1.action='store' 默认类型，可以忽略不写。用户必须给出一个明确的参数值，该类型定义了将实际参数值保存到dest指定变量中
    2.action='store_true' 用户不需给出参数值，该类型定义了将布尔值true保存到dest指定的变量中
    3.action='store_false' 用户不需给出参数值，该类型定义了将布尔值false保存到dest指定的变量中

args:返回一个位置参数的列表,也就是说不以任何长短名称开头的参数.这些参数放到 args 列表中

#-u,--user 表示一个是短选项 一个是长选项
#dest='user' 将该用户输入的参数保存到变量user中，可以通过options.user方式来获取该值
#type=str，表示这个参数值的类型必须是str字符型，如果是其他类型那么将强制转换为str（可能会报错）
#metavar='user'，当用户查看帮助信息，如果metavar没有设值，那么显示的帮助信息的参数后面默认带上dest所定义的变量名
#help='Enter..',显示的帮助提示信息
#default=3306，表示如果参数后面没有跟值，那么将默认为变量default的值

'''
from optparse import OptionParser


def main():
    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage=usage, version="%hsw 1.0")
    parser.add_option('-u', '--user', dest='user', action='store', type=str, metavar='user', help='Enter User Name!!')
    parser.add_option('-p', '--port', dest='port', type=int, metavar='xxxxx', default=3306, help='Enter Mysql Port!!')
    parser.add_option("-f", "--file", dest="filename",help="read data from FILENAME")
    parser.add_option("-v", "--verbose",action="store_true", dest="verbose")

    (options, args) = parser.parse_args()
    print 'OPTIONS: ', options
    print 'ARGS: ', args

    print '~' * 40
    print 'user: ', options.user
    print 'port: ', options.port
    print 'filename: ',options.filename
    print '~' * 40

    if options.verbose:
        print "reading %s..." % options.filename


if __name__ == '__main__':
    main()

'''
ocalhost:learnOptparse hushiwei$ python basic01.py -uroot -p3306 -fdemo.txt hello world
OPTIONS:  {'filename': 'demo.txt', 'verbose': None, 'port': 3306, 'user': 'root'}
ARGS:  ['hello', 'world']
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
user:  root
port:  3306
filename:  demo.txt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''
