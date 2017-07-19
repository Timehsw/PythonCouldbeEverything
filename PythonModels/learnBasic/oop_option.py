# coding=utf8
__author__ = 'zenith'
class Person():
    id=0
    name=""

    def __init__(self,_id,_name):
        self.id=_id
        self.name=_name
    def say(self):
        print("id:%s name:%s"%(self.id,self.name))
    def pl(self):
        print "ddddddddddd"

class Man():
    man="default"

    def __init__(self,_man):
        self.man=_man
    def sayMan(self):
        print("man:%s"%self.man)

p=Person(1,"zenith")
p.say()


class Student(Person):
    address=''
    def say(self):
        print("id:%s name:%s address:%s"%(self.id,self.name,self.address))
        print self.pl()

    def __init__(self, _id, _name,_address):
        Person.__init__(self,_id,_name)
        self.address=_address


s=Student('2','student','add')
s.say()


m=Man('m')
m.sayMan()


class Teacher(Person,Man):
    tea=''
    def sayMan(self):
        Man.sayMan(self)

    def say(self):
        Person.say(self)

    def __init__(self, _id, _name,_man,_tea):
        Person.__init__(self, _id, _name)
        Man.__init__(self,_man)
        self.tea=_tea


t=Teacher('id',10,'mans','tttt')
t.say()
t.sayMan()


