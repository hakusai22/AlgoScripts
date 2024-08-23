# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/7/10 19:29

if __name__ == '__main__':
    x = lambda a, b: a * b
    print(x(5, 6))  # prints '30'

    x = lambda a: a * 3 + 3
    print(x(3))  # prints '12'
