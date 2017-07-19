# coding=utf8
__author__ = 'zenith'

def no_option(x):
    pass

def normal(x=1):
    return x



def mutil(x=1,y=1):
    return 2*x,3*y


#print(mutil())

#本地测试
#print(__name__)
if __name__ =="__main__":
    print(mutil(y=2))