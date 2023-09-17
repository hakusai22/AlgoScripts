# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/10/31 23:38
import sys

if __name__ == '__main__':
    for line in sys.stdin:
        print(sum(map(int, line.split())))
