# coding=utf8
__author__ = 'zenith'

crxy="超人学院"
print(crxy)
crxynew1=crxy.decode("utf-8")
crxynew2=crxy.decode("gbk")
print(crxynew1)
print(crxynew2)

print(isinstance(crxynew2,unicode))


crxynew11=crxynew1.encode("utf-8")
crxynew12=crxynew2.encode("gbk")
print(crxynew11)
print(crxynew12)

##strip

s="aabc,defghe,llo,world\teee"

# print(s.strip("dao"))
# print(s.strip())
# print(s.split(',',2))
#
# print(s.split())
print(s)
print(s.replace('a','A',1))

l=["a","b","c"]
print("*".join(l))


print(s.find("e",7,13))

result="hello%sworld%s"%("zenith","hhh")
print(result)


