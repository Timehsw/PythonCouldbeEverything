# coding=utf8
__author__ = 'zenith'

def todo():
    try:
        i=10/0
        print("try")
    except Exception as e:
        #raise
        print e.message
    # finally:
    #     print("finally")
todo()
