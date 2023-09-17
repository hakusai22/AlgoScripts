# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/10 22:56
import sys

from python3语法基础.Py速成.面试.User2 import User2


class User1:
    def __init__(self, id, name, sex, status):
        self.id = id
        self.name = name
        self.sex = sex
        self.status = status


if __name__ == '__main__':
    u1 = User1('01', 'rocky', '男', 1)
    print(u1)
    u2 = User2('02', 'leey', '男', 1)
    print(u2)
    print(set(dir(u1)) - set(dir(u2)))
    print(u1.__dict__)
    print(sys.getsizeof(u1.__dict__))
