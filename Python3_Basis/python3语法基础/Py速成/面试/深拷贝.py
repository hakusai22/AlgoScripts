# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/10 22:53
import copy

if __name__ == '__main__':
    a = [1, 2, "hello", ['python', 'C++']]
    b = copy.deepcopy(a)
    print(b)
    print(a is b)
