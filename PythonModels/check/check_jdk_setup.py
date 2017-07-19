#! /usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'zenith'
import sys
import json
import check_util as cu


def check_jdk():
    # 初始分数0
    score = 0
    # 检测信息list [dict]
    list = []
    # 调用shell命令返回执行的结果output和执行状态值status
    cmd = "java -version"
    score, output = cu.check_score_contains_msg(score, 100, cmd, "Java(TM) SE Runtime Environment")
    list.append(output)
    return cu.result_format(score, list)

# 调用返回结果
if __name__ == '__main__':
    result = check_jdk()
    sys.stdout.write(json.dumps(result))
