# -*- coding: utf-8 -*-
"""
Created by hushiwei on 17-1-10.
"""

class demo1():
    name='tom'
    age=1
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print self.age,self.name


d=demo1(name='jj',age=4)
d.show()

print demo1.name