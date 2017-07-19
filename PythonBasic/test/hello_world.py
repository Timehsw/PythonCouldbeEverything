# coding=utf8
__author__ = 'zenith'

a=1
if a>0:
    print(a)
else:
    print(0-a)

#这是注释
print(None)

print(a is not None)


a=1
a=1.3
a=True
a="好的"
print(a)
print(r"aa\taa")

print(type(None))
print(isinstance(1.2,int))
print(type(a.decode('utf-8')))
print('ss1DDDf'.lower())
print('abcdef'.strip('ea'))
print('ss,dfsf,s,f,sf,s,f'.split(',',2))
print('ss,dfsf,s,f,sf,s,f'.replace('s','S',2))

print('qsddddd'.find('sd',2))

print('hello%s%s')%('zenith','yes')

a=[1,2,3]
print(a[1])
b=[3,4]
b.extend(a)




b.sort(cmp=lambda x,y:y-x,key=lambda x:-x,reverse=True)
b.remove(3)
print(b)


s=set([1,3,4,5])
for i in s:
    print(i)



sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
    if n==97:
        continue
print(sum)
#continue结束本次循环继续下一次
#break终止所有循环
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
print(move(1,2,step=2))



a=[1,2,3]
print(a[1])
b=[3,4]
b.extend(a)

print(b)
print(b[-3:-1])




print([x+y for x in 'ABC' for y in 'abc'])

dic={"a":"A","b":"B"}
for key,value in dic.items():
    print(key,value)

file=open('D:\data.txt','r')
#print(file.read())
for line in file.readlines():
    print(line.strip())


