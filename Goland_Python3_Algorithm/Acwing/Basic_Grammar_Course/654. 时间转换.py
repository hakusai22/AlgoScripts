# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/11/1 00:16

if __name__ == '__main__':
    a = int(input())
    print("%d:%d:%d" % (a // 3600, a % 3600 // 60, a % 60))
