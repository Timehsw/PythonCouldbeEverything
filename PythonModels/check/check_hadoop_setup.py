#! /usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'zenith'

import sys
import json
import check_jdk_setup as jdk
import check_util as cu
# 初始分数0
score = 0
# 检测信息list [dict]
list = []
# 步骤1：检查jdk是否安装完毕 10分
jdk_check = jdk.check_jdk()
if jdk_check[0].get("score", 0) == 100:
    score += 10
# 添加检测信息
list.append(jdk_check[1][0])

# 步骤2 zk安装检测 20分
cmd = "jps | grep QuorumPeerMain | wc -l"
score, output = cu.check_score_equal_msg(score, 20, cmd, "1")
list.append(output)

# 步骤3 hdfs 40分
cmd = "hdfs dfs -ls /"
score, output = cu.check_score_not_contains_msg(score, 40, cmd, "hdfs: command not found")
list.append(output)

# 步骤3 hdfs 30分
cmd = "jps | grep ResourceManager | wc -l"
score, output = cu.check_score_equal_msg(score, 30, cmd, "1")
list.append(output)

# 返回结果
sys.stdout.write(json.dumps(cu.result_format(score, list)))
