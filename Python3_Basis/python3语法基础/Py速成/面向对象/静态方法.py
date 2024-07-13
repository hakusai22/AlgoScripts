# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/9/29 09:40

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hell(self):
        print("AAA{},{}".format(self.name, self.age))

    @staticmethod
    def he():
        print("静态方法")


if __name__ == '__main__':
    jack = Student('Java', 12)
    Student.he()
    jack.he()
