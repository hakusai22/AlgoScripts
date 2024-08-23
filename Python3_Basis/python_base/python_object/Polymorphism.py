# --idea
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2023/12/11 15:02


class Animal:

    def kind(self):
        print("i am animal")


class Dog(Animal):

    def kind(self):
        print("i am a dog")


class Cat(Animal):

    def kind(self):
        print("i am a cat")


class Pig(Animal):

    def kind(self):
        print("i am a pig")

# 这个函数接收一个animal参数，并调用它的kind方法
def show_kind(animal):
    animal.kind()


if __name__ == '__main__':
    d = Dog()
    c = Cat()
    p = Pig()

    show_kind(d)
    show_kind(c)
    show_kind(p)