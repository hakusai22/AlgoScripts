# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/7/10 21:14


from itertools import *
from debugpy.common.compat import izip

if __name__ == '__main__':
    for i in izip([1, 2, 3], ['a', 'b', 'c']):
        print(i)
    # ('a', 1)
    # ('b', 2)
    # ('c', 3)

    for i in izip(count(1), ['Bob', 'Emily', 'Joe']):
        print(i)
    # (1, 'Bob')
    # (2, 'Emily')
    # (3, 'Joe')

    def check_for_drop(x):
        print('Checking: ', x)
        return x > 5


    for i in dropwhile(check_for_drop, [2, 4, 6, 8, 10, 12]):
        print('Result: ', i)
    # Checking: 2
    # Checking: 4
    # Result: 6
    # Result: 8
    # Result: 10
    a = sorted([1, 2, 1, 3, 2, 1, 2, 3, 4, 5])
    for key, value in groupby(a):
        print((key, value), end='')
        # (1, [1, 1, 1])
        # (2, [2, 2, 2])
        # (3, [3, 3])
        # (4, [4])
        # (5, [5]
