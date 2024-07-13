# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/11/1 00:11


if __name__ == '__main__':
    x1, y1 = map(lambda x: float(x), input().split(" "))
    x2, y2 = map(lambda x: float(x), input().split(" "))

    res = (x2 - x1) ** 2 + (y2 - y1) ** 2
    print("{:.4f}".format(res ** 0.5))
