# --idea
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2023/12/11 15:02

class Student:
    classroom = '101'
    address = 'beijing'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_age(self):
        print('%s: %s' % (self.name, self.age))

if __name__ == '__main__':
    stu = Student("1", 1)
    print(stu.name)
    print(stu.classroom)
