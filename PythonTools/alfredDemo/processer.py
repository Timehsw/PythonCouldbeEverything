# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/11/10.
'''

import os
import json


def json_feedback(ip, title, subtitle):
    argReturn = "%s: %s %s " % (ip, title, subtitle)
    res = {
        "title": title,
        "subtitle": subtitle,
        "arg": argReturn,
        "icon": "icon.png"
    }

    outputStr = json.dumps({"items": [res]})
    return outputStr


def process():
    notice('请先设置七牛相关配置')


def notice(msg, title="上传图片到七牛云通知"):
    os.system('osascript -e \'display notification "{}" with title "{}"\''.format(msg, title))


def open_with_editor(file_path):
    os.system('open -e "./{}"'.format(file_path))


def main(work):
    """main"""
    process()
    print json_feedback("123", work, "789")


if __name__ == '__main__':
    # work = u'{query}'
    work = u'123'
    main(work)