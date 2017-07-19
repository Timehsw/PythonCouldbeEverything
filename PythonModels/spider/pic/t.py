# -*- coding: utf-8 -*-
__author__ = 'zenith'

import re
import json
import codecs
import socket
import httplib
from HTMLParser import HTMLParser

HOST = 'jiance.tianjinep.com'
START_PATH = '/plus/list.php?tid=107'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36'
ACCEPT = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'

XPATH_ID_PATTERN = re.compile('^(//\*\[@id="(\S+)"\]/)')
XPATH_ARRAY_PATTERN = re.compile('.+\[(\d+)\]')
COMPANY_LINK_PATTERN = re.compile('(http://jiance.tianjinep.com)?/plus/list.php\?tid=(\d+)')
DATETIME_PATTERN = re.compile('(\d\d\d\d)-(\d\d)-(\d\d) (\d\d):(\d\d)')
DATE_PATTERN = re.compile('(\d\d\d\d)-(\d\d)-(\d\d)')
TIME_PATTERN = re.compile('(\d\d):(\d\d)')

IGNORE_TAGS = ['link', 'br', 'meta', 'img', 'area', 'input', 'form']

COMPANY_TBODY = '/html/body/div[3]/div/table[2]/tbody/tr[2]/td/table/tbody'
MONITOR_LINKS_DIV = '/html/body/div[3]/div'
CLASS_RIGHT_DIV = '/html/body/div[3]'
MONITOR_POINT = '/tr[2]/td[1]'
MONITOR_TIME = '/tr[2]/td[2]'
PLAIN_TD = '/tr[4]/td[2]'
HORIZON_T1_TD = '/tr[2]/td[3]'
HORIZON_T2_TD = '/tr[2]/td[4]'
HORIZON_T3_TD = '/tr[2]/td[5]'
VERTICAL_T1_TD = '/tr[4]/td[3]'
VERTICAL_T2_TD = '/tr[5]/td[1]'
VERTICAL_T3_TD = '/tr[6]/td[1]'


class Company():
    def __init__(self):
        self.id = ''  # 主键
        self.company_name = ''  # 企业（公司）名称
        self.org_code = ''  # 法人代码（组织机构代码）
        self.legal_person = ''  # 法人代表（企业法人）
        self.tech_person = ''  # 联系人（环保专工）
        self.contact = ''  # 办公电话（联系方式）
        self.source_name = ''  # 污染源名称
        self.source_type = ''  # （国控类型）企业类别
        self.area = ''  # 所属行政区（地区）
        self.source_property = ''  # 监控级别（重点源属性）
        self.industry = ''  # （所属行业）行业类别
        self.adress = ''  # （企业地址）地理位置
        self.postal = ''  # 邮编
        self.lat = ''  # 中心纬度
        self.lng = ''  # 中心经度
        self.glat = ''  # 谷歌纬度
        self.glng = ''  # 谷歌经度
        self.blat = ''  # 百度纬度
        self.blng = ''  # 百度经度
        self.period = ''  # 生产周期


class MonitorPoints():
    def __init__(self):
        self.company_id = ''  # 外键关联到公司表，代表这个监测点是所关联的公司的
        self.id = ''
        self.name = ''  # 监测点位名称
        self.code = ''
        self.release_mode = ''
        self.release_type = ''
        self.release_destination = ''
        self.delegation = ''
        self.delegation_company = ''
        self.quality_control = ''
        self.position_picture = ''
        self.position_picture_url = ''
        self.device_name = ''


class MonitorInfos():
    def __init__(self):
        self.monitor_point_id = ''  # 外键关联到监测站点id
        self.id = ''
        self.index = ''  # COD， 氨氮等
        self.frequency = ''  # 自动是每两小时，手工月，还有季度
        self.max = ''  # 标准值这一列有
        self.max_unit = ''  # 大部分是mg/L
        self.min = ''  # 自动，手动
        self.min_unit = ''
        self.source = ''
        self.way = ''
        self.publish_due = ''


class Results():
    def __init__(self):
        self.monitor_point_id = ''  # 解析并关联到具体的某个公司的某个监测点上
        self.type = ''  # 有时均值，日均值，月均值，季度等，用 hour, day, month,quarter，year 标示
        self.index_id = ''  # 解析并关联到某个公司的某个监测点的某个监测指标上
        self.index_name = ''  # 为便于比对和调试，结果的名称，比如二氧化硫，也存放在此表中
        self.min_cal_value = ''  #
        self.value = ''  # 具体的该监测指标的值。 折算后的值放在这个里面
        self.max_cal_value = ''
        self.release_time = ''  # 网页上显示的时间，但作为时间格式存入数据库
        self.monitor_way = ''  # auto/manual,用于区分手工还是自动化结果
        self.exceed_flag = ''
        self.exceed_type = ''  # 超上限还是超下限  1.1版本增加
        self.times = ''  # 超标倍数  1.1版本增加
        self.data_status = ''
        self.remark = ''


class Node():
    def __init__(self, tag, attrs=None, data=None):
        self.tag = tag
        self.attrs = {}
        if attrs:
            for (k, v) in attrs:
                self.attrs[k] = v
        self.data = data
        if self.data is None:
            self.data = ''

        self.parent = None
        self.children = None
        self.next_node = None
        self.pre_node = None

    def append(self, node):
        if self.children is None:
            self.children = []
        self.children.append(node)
        node.parent = self

    def link_next_pre(self):
        if not self.children:
            return
        i = 0
        length = len(self.children)
        while i < length:
            if i < length - 1:
                self.children[i].next_node = self.children[i + 1]
            if i > 0:
                self.children[i].pre_node = self.children[i - 1]
            i = i + 1

    def get_parent_node(self, tag):
        node = self
        while node.parent is not None:
            if node.parent.tag == tag:
                return node.parent
            node = node.parent
        return None

    def get_all_data(self):
        datas = []
        datas.append(self.data)
        if self.children:
            for child in self.children:
                datas.append(child.get_all_data().strip())
        return ''.join(datas).strip()


class SpiderHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.ids = {}
        self.root = Node('ROOT')
        self.current = self.root
        self.empty_node = Node('empty')

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag in IGNORE_TAGS:
            return
        parent = self.current
        self.current = Node(tag, attrs=attrs)
        parent.append(self.current)
        if not attrs or 'id' not in attrs:
            return
        self.ids[attrs['id']] = self.current

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in IGNORE_TAGS:
            return
        self.current.link_next_pre()
        self.current = self.current.parent

    def handle_data(self, data):
        if self.current and data:
            if type(data) is unicode:
                data = data.encode('utf-8')
            self.current.data = self.current.data + data.strip()

    # support:
    # //*[@id="items1_1"]/ul/li[1]/div/div[2]/a
    # /html/body/div[3]/div/table[2]/tbody/tr[2]/td/table/tbody/tr[9]/td[3]/label
    def get_node(self, xpath):
        pnode = self.root
        m = XPATH_ID_PATTERN.match(xpath)
        if m:
            id_xpath = m.group(1)
            _id = m.group(2)
            # print '_id: %s' % _id
            pnode = self.get_node_by_id(_id)
            # print pnode
            # print 'id_xpath: %s' % id_xpath
            xpath = '/' + xpath[len(id_xpath):]
            # print 'xpath: %s' % xpath
        return self.get_node_by_pnode_xpath(pnode, xpath)

    def get_node_by_id(self, _id):
        if _id not in self.ids:
            return None
        return self.ids[_id]

    def get_node_by_pnode_xpath(self, pnode, xpath):
        if not pnode:
            return self.empty_node
        for x in xpath.split('/'):
            if x is None or x == '':
                continue
            tag = x;
            index = 0
            m = XPATH_ARRAY_PATTERN.match(x)
            # print 'XPATH_ARRAY_PATTERN.match(%s)' % x
            if m:
                tag = x[0:x.rindex('[')]
                index = int(m.group(1)) - 1
            # print 'pnode: %s, %s' % (pnode, pnode.tag)
            # print 'x: %s' % x
            # print 'tag: %s' % tag
            # print 'index: %s' % index
            if pnode.children is None:
                # print 'pnode.children is None'
                return self.empty_node
            for child in pnode.children:
                # print child.tag, tag
                if child.tag == tag:
                    # print 'child.tag == tag'
                    # print 'index'
                    index = index - 1
                if index == -1:
                    # print child.tag
                    pnode = child
                    break
            if index != -1:
                return self.empty_node
        if pnode is None:
            return self.empty_node
        return pnode

    def filter(self, node, filter_def):
        results = []
        nodes = [node]
        while len(nodes) > 0:
            new_nodes = []
            for node_iter in nodes:
                if filter_def(node_iter):
                    results.append(node_iter)
                if not node_iter.children:
                    continue
                for x in node_iter.children:
                    new_nodes.append(x)
            nodes = new_nodes
        return results

    # debug
    def printTree(self, node):
        nodes = [node]
        while len(nodes) > 0:
            print '------------------'
            new_nodes = []
            for node_iter in nodes:
                print node_iter, node_iter.tag, node_iter.attrs, node_iter.data
                if not node_iter.children:
                    continue
                for x in node_iter.children:
                    new_nodes.append(x)
            nodes = new_nodes


class Spider():
    def __init__(self):
        self.parser = SpiderHTMLParser()

    def start(self):
        html = self.request('GET', HOST, START_PATH, '')
        if html is None:
            self.warn()
            return
        self.parser.feed(html)
        company_links = self.get_all_company_links()
        link_set = set()
        for company_name, link in company_links:
            if link in link_set:
                continue
            link_set.add(link)
            # print 'get company: %s, url: %s' % (company_name, link)
            html = self.request('GET', HOST, link, '')
            if html is None:
                self.warn()
                return
            self.parser = SpiderHTMLParser()
            self.parser.feed(html)
            self.get_company_infos()
            monitor_links = self.get_monitor_links()
            for monitor, result_link in monitor_links:
                print monitor, result_link
                m = COMPANY_LINK_PATTERN.match(result_link)
                if not m:
                    continue
                tid = m.group(2)
                # tid = 96
                # tid = 877
                #tid = 325
                #result_html = codecs.open('D:\\proc\\cr_python\\cn\\zenith\\spider\\%s.html' % tid, encoding='gbk', mode='r').read()
                result_html=self.request('GET', HOST, result_link, '')
                parser = SpiderHTMLParser()
                parser.feed(result_html)
                class_right_node = parser.get_node(CLASS_RIGHT_DIV)
                if class_right_node is None or class_right_node == parser.empty_node:
                    print 'class_right_node not found'
                    continue
                td_nodes = parser.filter(class_right_node, filter_td_with_background_tbg_gif)
                if len(td_nodes) == 0:
                    print 'filter_td_with_background_tbg_gif not found'
                    continue
                result_table_node = td_nodes[0].get_parent_node('table')
                if result_table_node is None:
                    print 'result_table_node not found'
                    continue
                # print result_table_node.tag
                # for x in result_table_node.children:
                #    print x.tag
                monitorPoint = parser.get_node_by_pnode_xpath(result_table_node, MONITOR_POINT)
                monitorTime = parser.get_node_by_pnode_xpath(result_table_node, MONITOR_TIME)
                print monitorPoint, monitorTime
                if monitorPoint == parser.empty_node or monitorTime == parser.empty_node:
                    print 'monitorPoint or monitorTime not found'
                    continue
                point = monitorPoint.get_all_data()
                datetime = monitorTime.get_all_data()
                if point != '监测点位' or datetime != '监测日期':
                    print point, datetime
                    continue
                fomat_type = ''

                t1 = parser.get_node_by_pnode_xpath(result_table_node, PLAIN_TD)
                print t1 == parser.empty_node
                if t1:
                    d1 = t1.get_all_data()
                    print d1
                    if d1:
                        d1 = d1.replace('：', ':').strip()
                    if DATETIME_PATTERN.match(d1):
                        fomat_type = 'plain_table'
                        print fomat_type
                        # TODO
                        self.handle_plain_table(parser, result_table_node)
                        continue
                t1 = parser.get_node_by_pnode_xpath(result_table_node, HORIZON_T1_TD)
                t2 = parser.get_node_by_pnode_xpath(result_table_node, HORIZON_T2_TD)
                t3 = parser.get_node_by_pnode_xpath(result_table_node, HORIZON_T3_TD)
                if t1 and t2 and t3:
                    (d1, d2, d3) = (t1.get_all_data(), t2.get_all_data(), t3.get_all_data())
                    print (d1, d2, d3)
                    if d1 and d2 and d3:
                        (d1, d2, d3) = (d1.replace('：', ':').replace(' ', ''), d2.replace('：', ':').replace(' ', ''),
                                        d3.replace('：', ':').replace(' ', ''))
                    print (d1, d2, d3)
                    if TIME_PATTERN.match(d1) and TIME_PATTERN.match(d2) and TIME_PATTERN.match(d3):
                        fomat_type = 'horizon_table'
                        print fomat_type
                        colspan = 1
                        if 'colspan' in t1.attrs:
                            colspan = int(t1.attrs['colspan'])
                        self.handle_horizon_table(parser, result_table_node, colspan)
                        # TODO
                        continue
                t1 = parser.get_node_by_pnode_xpath(result_table_node, VERTICAL_T1_TD)
                t2 = parser.get_node_by_pnode_xpath(result_table_node, VERTICAL_T2_TD)
                t3 = parser.get_node_by_pnode_xpath(result_table_node, VERTICAL_T3_TD)
                if t1 and t2 and t3:
                    (d1, d2, d3) = (t1.get_all_data(), t2.get_all_data(), t3.get_all_data())
                    print (d1, d2, d3)
                    if d1 and d2 and d3:
                        (d1, d2, d3) = (d1.replace('：', ':').replace(' ', ''), d2.replace('：', ':').replace(' ', ''),
                                        d3.replace('：', ':').replace(' ', ''))
                    print (d1, d2, d3)
                    if TIME_PATTERN.match(d1) and TIME_PATTERN.match(d2) and TIME_PATTERN.match(d3):
                        fomat_type = 'vertical_table'
                        print fomat_type
                        # TODO
                        self.handle_vertical_table(parser, result_table_node)
                        continue

    def handle_plain_table(self, parser, table_node):
        mtypes = []
        for i in range(0, 10):
            mtype = parser.get_node_by_pnode_xpath(table_node, '/tr[2]/td[%s]' % (i + 3))
            if not mtype or mtype == parser.empty_node:
                break
            mtypes.append(mtype.get_all_data().strip())
        print mtypes
        for x in range(4, 10000):
            mpoint = parser.get_node_by_pnode_xpath(table_node, '/tr[%s]/td[%s]' % (x, 1))
            mdatetime = parser.get_node_by_pnode_xpath(table_node, '/tr[%s]/td[%s]' % (x, 2))
            if not mpoint or not mdatetime or mpoint == parser.empty_node or mdatetime == parser.empty_node:
                break
            values = []
            for y in range(0, len(mtypes)):
                value = parser.get_node_by_pnode_xpath(table_node, '/tr[%s]/td[%s]' % (x, (y + 3)))
                if not value:
                    continue
                values.append(value.get_all_data().strip())
            if len(values) != len(mtypes):
                break
            print mpoint.data, mdatetime.data, values

    def handle_horizon_table(self, parser, table_node, colspan):
        for x in range(5, 10000):
            mpoint = parser.get_node_by_pnode_xpath(table_node, '/tr[%s]/td[%s]' % (x, 1))
            mdate = parser.get_node_by_pnode_xpath(table_node, '/tr[%s]/td[%s]' % (x, 2))
            if not mpoint or not mdate or mpoint == parser.empty_node or mdate == parser.empty_node:
                break
            mtime = None
            for y in range(3, 100):
                value = parser.get_node_by_pnode_xpath(table_node, '/tr[%s]/td[%s]' % (x, y))
                if not value or value == parser.empty_node:
                    break
                mtype = parser.get_node_by_pnode_xpath(table_node, '/tr[%s]/td[%s]' % (3, y - 2))
                mtime = parser.get_node_by_pnode_xpath(table_node, '/tr[%s]/td[%s]' % (2, 3 + (y - 3) / colspan))
                print mpoint.data, mdate.data, mtime.data, mtype.get_all_data(), value.get_all_data()

    def handle_vertical_table(self, parser, table_node):
        mpoint = parser.get_node_by_pnode_xpath(table_node, '/tr[%s]/td[%s]' % (5, 1))
        mpoint = None
        mdate = None
        for x in range(4, 10000):
            t1 = parser.get_node_by_pnode_xpath(table_node, '/tr[%s]/td[%s]' % (x, 1))
            t2 = parser.get_node_by_pnode_xpath(table_node, '/tr[%s]/td[%s]' % (x, 2))
            if not t1 or not t2 or t1 == parser.empty_node or t2 == parser.empty_node:
                break
            start = 1
            if DATE_PATTERN.match(t2.data):
                mpoint = t1.data
                mdate = t2.data
                start = 3
            mtime = None
            for y in range(start, 100):
                t3 = parser.get_node_by_pnode_xpath(table_node, '/tr[%s]/td[%s]' % (x, y))
                if not t3 or t3 == parser.empty_node:
                    break
                if TIME_PATTERN.match(t3.data):
                    mtime = t3.data
                    continue
                z = y
                if start == 1:
                    z = y + 2
                mtype = parser.get_node_by_pnode_xpath(table_node, '/tr[2]/td[%s]' % z)
                print mpoint, mdate, mtime, mtype.get_all_data(), t3.get_all_data()

    def stop(self):
        pass

    def resume(self):
        pass

    def get_company_infos(self):
        company_name = self.parser.get_node(COMPANY_TBODY + '/tr[3]/td[3]/label').data
        source_type = self.parser.get_node(COMPANY_TBODY + '/tr[3]/td[5]').data
        source_property = self.parser.get_node(COMPANY_TBODY + '/tr[3]/td[7]').data
        area = self.parser.get_node(COMPANY_TBODY + '/tr[4]/td[5]').data
        industry = self.parser.get_node(COMPANY_TBODY + '/tr[4]/td[7]').data
        period = self.parser.get_node(COMPANY_TBODY + '/tr[5]/td[5]').data
        adress = self.parser.get_node(COMPANY_TBODY + '/tr[10]/td[5]').data
        tech_person = self.parser.get_node(COMPANY_TBODY + '/tr[9]/td[3]/label').data
        contact = '%s %s' % (self.parser.get_node(COMPANY_TBODY + '/tr[9]/td[5]').data,
                             self.parser.get_node(COMPANY_TBODY + '/tr[9]/td[7]').data)
        legal_person = self.parser.get_node(COMPANY_TBODY + '/tr[10]/td[3]').data

        # print company_name, source_type, source_property, area, industry, period, adress, tech_person, contact, legal_person
        return company_name, source_type, source_property, area, industry, period, adress, tech_person, contact, legal_person

    def get_all_company_links(self):
        company_links = []
        nodes = self.parser.filter(self.parser.get_node('/html/body/div[2]'), filter_company_link)
        for node in nodes:
            if 'href' not in node.attrs or not COMPANY_LINK_PATTERN.match(node.attrs['href']):
                continue
            company_links.append((node.data, node.attrs['href']))
        company_links.sort()
        return company_links

    def get_monitor_links(self):
        monitor_links = []
        nodes = []
        node = None
        for x in range(1, 10):
            for y in range(1, 10):
                node = self.parser.get_node(MONITOR_LINKS_DIV + '/ul[%s]/li[%s]/a' % (x, y))
                if node is None or node == self.parser.empty_node:
                    break
                nodes.append(node)
        for node in nodes:
            if 'href' in node.attrs and COMPANY_LINK_PATTERN.match(node.attrs['href']):
                monitor_links.append((node.data, node.attrs['href']))
        monitor_links.sort()
        return monitor_links

    def request(self, method, host, path, params):
        headers = {'Host': host, 'User-Agent': USER_AGENT, 'Accept': ACCEPT}
        conn = None
        for x in [0, 1, 2]:
            try:
                conn = httplib.HTTPConnection(host, port=80, timeout=10)
                conn.request(method, path, params, headers)
                response = conn.getresponse()
                data = response.read()
                return data.decode('gbk').encode('utf-8')
            except Exception, e:
                print e
            finally:
                if conn:
                    conn.close()
        return None

    def warn(self):
        pass


def filter_company_link(node):
    if node.tag == 'a' and node.data and node.attrs is not None:
        if 'href' in node.attrs and COMPANY_LINK_PATTERN.match(node.attrs['href']):
            return True
    return False


def filter_td_with_background_tbg_gif(node):
    if node.tag == 'td':
        if 'background' in node.attrs and node.attrs['background'] == 'images/tbg.gif':
            return True
    return False


if __name__ == '__main__':
    spider = Spider()
    spider.start()
    # parser = SpiderHTMLParser()
    # with codecs.open('/tmp/t.html', encoding='gbk', mode='r') as html:
    #    parser.feed(html.read())
    # parser.feed('<td width="70">二氧化硫<br />(mg/m<sup>3</sup>)</td>')
    # company_link_nodes = parser.filter(parser.get_node('/html/body/div[2]'), filter_company_link)


    # company_dict = {'company_name': company_name, 'source_type': source_type, 'source_property': source_property, 'area': area, 'industry': industry, 'period': period, 'adress': adress, 'tech_person': tech_person, 'contact': contact, 'legal_person': legal_person}

    # print json.dumps(company_dict)

    # print parser.printTree(parser.root)
    # print parser.get_node('//*[@id="items2_1"]/ul/li[1]/div/div[2]/a').data
    # print parser.get_node('//*[@id="items3_1"]/ul/li[12]/div/div[2]/a').data
