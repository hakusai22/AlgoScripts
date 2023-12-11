# --idea
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2023/12/11 15:02

# 父类定义
class people:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))

# 单继承示例
class student(people):

    def __init__(self, name, age, weight, grade):
        # 调用父类的实例化方法
        people.__init__(self, name, age, weight)
        self.grade = grade

    # 重写父类的speak方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))

if __name__ == '__main__':
    s = student('ken', 10, 30, 3)
    s.speak()
