# coding=utf8
__author__ = 'zenith'
import ConfigParser as cpr
cp=cpr.ConfigParser()
cp.read("D:\passwd")

cp.set("users","testnew","3344")
#cp.add_section("usersnew")
cp.set("usersnew","test","3344")
cp.remove_section("users")
# print(cp.sections())
# print(cp.options("users"))
# print(cp.items("users"))

cp.write(open("D:\passwd","w"))
