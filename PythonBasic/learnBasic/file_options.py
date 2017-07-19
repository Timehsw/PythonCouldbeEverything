# coding=utf8
__author__ = 'zenith'

#读文件
f=open("D:\data.txt","r")
#print(f.read())
#print(f.readline().strip())
#print(f.readline().strip())

for line in f.readlines():
    print(line.strip())
f.close()

#文件追加内容
f=open("D:\data.txt","a")
f.write("\n超人学院")
f.close()


#文件覆盖内容
f=open("D:\data.txt","w")
f.write("\n超人学院")
f.close()
