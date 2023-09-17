# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/9/29 09:33

class Student(object):
    school = '东方小学'  # 类变量

    def __init__(self, name, age):
        self.name = name  # 实例变量
        self.age = age  # 实例变量

    def hello(self):
        print('你好，我是{}，今年{}岁'.format(self.name, self.age))

    @classmethod
    def print_school(cls):  # 类方法
        print(cls.school)


if __name__ == '__main__':
    jack = Student('Jack', 18)
    tom = Student('Tom', 20)
    jack.print_school()
    tom.print_school()

    Student.school = '东明小学'  # 修改类变量
    jack.print_school()  # 东明小学
    tom.print_school()  # 东明小学
