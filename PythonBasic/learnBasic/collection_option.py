# coding=utf8
__author__ = 'zenith'
#list
# l=[1,2,3,4,5]
# m=list()
# m=list(l)
#
# print(m)
# print(type(l))
#
# l.append(6)
# l.insert(6,10)
# l.pop()
# l.pop(2)
# l[3]=99
# print(l)

"""
l=['am','b','c','d','e','e','g']
m=['b','c']
m.extend(l)
m.count('c')
m.index('c')
m.reverse()

m.remove('c')


ss=['a','b','cc','d']
print(ss)
def cmp_funtion(x,y):
    return x-y

def key_function(x):
    return len(x)


ss.sort(cmp=lambda x,y:x-y,key=lambda x:len(x))
print(ss)
"""

# [11,13,14,12]
#[1,3,4,2]


#print(m)

#tuple

# t=(1,2,3)
# print(t[2])



#dict
"""
dic=dict()
dic={"k1":1,"k2":"zenith","k3":True}
dic["k4"]=[1,2,3]
dic['k1']=2
# print(dic["k6"])
print(dic.get("k1",0))
print(dic.get("k6",0))
dic.pop("k2")
dic.clear()
print(dic)
"""


#set
"""
s=set([1,2,3,3,3,4,5])
s.add(4)
s.add(6)
s.remove(2)
print(s)
"""

#list
for item in ["a","b","c"]:
    print(item)
#tuple
for item in ("a","b","c"):
    print(item)
#dict
for k in {"k1":1,"k2":"zenith","k3":True}.keys():
    print(k)

for v in {"k1":1,"k2":"zenith","k3":True}.values():
    print(v)

for key,value in {"k1":1,"k2":"zenith","k3":True}.items():
    print("key:%s value:%s"%(key,value))
#set
for item in set(["a","a","b","b"]):
    print(item)


#{"k1":1,"k2":"zenith","k3":True}
print "-----------------"
dic=dict()
dic["k1"]=1
dic["k2"]="zenith"
dic["k3"]=True
print(dic)
print(dic.items())

print(dic.keys())
print "-----------------"

for k in {1:1,"k":[1,2,3]}.keys():
    print(type(k))





age=10
if age>18:
    print("ok")
# else:
#     if age>10:
#         print("normal")
#     else:
#         print("no")
elif age>10:
    print("normal")
else:
    print("no")


#切片
l=['am','b','c','d','e','e','g']
print(l[5:1:-2])
#l[m:n:p] 从索引为m的元素开始取值每p个元素取一一直到n个索引但是不包含n对应的元素
# m,n,p都可取负值 m，n 负值表示倒数第几个  p为反方向方向
# m n :-2 -1 0 1 2 3可以任意组合
#取倒数第2个和倒数第4个
print(l[-4:-1:2])
print(l[-1:-5:-2])


#获取索引
for i,item in enumerate(l):
    print(i,item)

dic={"k1":1,"k2":"zenith","k3":True}
for i,k in enumerate(dic):
    print(i,k,dic[k])
    #print("index :%s key:%s value:%s"%(i,k,v))


#list gen
#[3,6,9,……]
print(range(1,11))

world=['a','b','c','d','e','f','g']
number=range(1,8)

print([3*x for x in range(1,11) if x%2==0 and x>3])
print([w+str(n) for w in world for n in number])



#生成器
g=(w+str(n) for w in world for n in number)
# print(g.next())
# print(g.next())

for i in g:
    print(i)



