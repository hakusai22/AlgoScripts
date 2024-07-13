# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/11/2 16:39
import collections

if __name__ == '__main__':
    list = [1, 123, 32423, 234234, 234234, 23423]
    cnt = collections.Counter(list)
    print(cnt)
