# coding=utf-8
__author__ = 'zenith'

"""这是中文"""


# 面向对象

class Person:
    name = ''

    def __init__(self, _name):
        self.name = _name

    def show(self):
        print("Person:%s" % self.name)


p = Person('zenith')
p.show()


class Student(Person):
    pass


# 默认调用父类的构造函数
s = Student('Mik')
s.show()


class Teacher(Person):
    def show(self):
        print("Teacher:%s" % self.name)


t = Teacher('super')
t.show()


class It:
    name = ''
    age = ''

    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

    def show(self):
        print("It:%s,%s" % (self.name, self.age))


class Muti( It,Person):
    pass

m=Muti('muti',11)
m.show()