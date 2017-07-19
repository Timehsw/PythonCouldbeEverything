# -*- coding: utf-8 -*-
"""
Created by hushiwei on 17-1-10.
"""

from collections import namedtuple
from flask_babel import lazy_gettext as _

Point=namedtuple('Point',['x','y'])
p=Point(1,2)
print p.x
Grain = namedtuple('Grain', 'name label function')
time_grains = (
    Grain('Time Column', _('Time Column'), '{col}'),
    Grain("second", _('second'), "DATE_ADD(DATE({col}), "
                                 "INTERVAL (HOUR({col})*60*60 + MINUTE({col})*60"
                                 " + SECOND({col})) SECOND)"),
    Grain("minute", _('minute'), "DATE_ADD(DATE({col}), "
                                 "INTERVAL (HOUR({col})*60 + MINUTE({col})) MINUTE)"),
    Grain("hour", _('hour'), "DATE_ADD(DATE({col}), "
                             "INTERVAL HOUR({col}) HOUR)"),
    Grain('day', _('day'), 'DATE({col})'),
    Grain("week", _('week'), "DATE(DATE_SUB({col}, "
                             "INTERVAL DAYOFWEEK({col}) - 1 DAY))"),
    Grain("month", _('month'), "DATE(DATE_SUB({col}, "
                               "INTERVAL DAYOFMONTH({col}) - 1 DAY))"),
    Grain("quarter", _('quarter'), "MAKEDATE(YEAR({col}), 1) "
                                   "+ INTERVAL QUARTER({col}) QUARTER - INTERVAL 1 QUARTER"),
    Grain("year", _('year'), "DATE(DATE_SUB({col}, "
                             "INTERVAL DAYOFYEAR({col}) - 1 DAY))"),
)
#
for t in time_grains:
    print t.name+" --- "+t.label+" --- "+t.function


# 变量名和namedtuple中的第一个参数一般保持一致，但也可以不一样
Student = namedtuple('Student', 'id name score')
# 或者 Student = namedtuple('Student', ['id', 'name', 'score'])

# students = [(1, 'Wu', 90), (2, 'Xing', 89), (3, 'Yuan', 98), (4, 'Wang', 95)]
#
# for s in students:
#     stu = Student._make(s)
#     print stu.name

s=Student(1,'hello world',45)
print s.name
print s.score
