# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/7/10 19:37

if __name__ == '__main__':
    def multiplier_func(a, b):
        return a * b


    def square_it_func(a):
        return a * a


    x = map(square_it_func, [1, 4, 7])

    print(list(x))  # prints  [1, 16, 49]

    x = list(map(multiplier_func, [1, 4, 7], [2, 5, 8]))

    print(list(x))  # [2, 20, 56]
