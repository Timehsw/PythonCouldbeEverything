# -*- coding: UTF-8 -*-
__author__ = 'zenith'
import commands


def cmd_output_f(cmd, output):
    """将命令和检测信息生成dict"""
    return {"cmd": cmd, "output": output}


def result_format(score, out_list):
    """将分数和检测信息list 生成结果list"""
    return [{"score": score}, out_list]


def check_score_equal_msg(score, point, cmd, msg):
    """执行结果和预期信息相等的检测"""
    try:
        status, output = commands.getstatusoutput(cmd)
        if status == 0 and output == msg:
            score += point
        result = output
    except Exception as e:
        result = e
    return score, cmd_output_f(cmd, result)


def check_score_contains_msg(score, point, cmd, msg):
    """执行结果包含预期信息相等的检测"""
    try:
        status, output = commands.getstatusoutput(cmd)
        if status == 0 and output.find(msg) > -1:
            score += point
        result = output
    except Exception as e:
        result = e
    return score, cmd_output_f(cmd, result)


def check_score_not_contains_msg(score, point, cmd, msg):
    """执行结果不包含预期信息相等的检测"""
    try:
        status, output = commands.getstatusoutput(cmd)
        if output.find(msg) == -1:
            score += point
        result = output
    except Exception as e:
        result = e
    return score, cmd_output_f(cmd, result)