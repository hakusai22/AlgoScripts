# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/9/29 09:51


class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)


if __name__ == '__main__':
    s = Square(4)
    print(s.area())
