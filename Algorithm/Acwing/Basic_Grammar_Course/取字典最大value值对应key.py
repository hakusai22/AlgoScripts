# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/11/2 16:58

from collections import Counter

if __name__ == '__main__':
    nums = [1, 2, 2, 2, 3, 4, 4]
    cnt = Counter(nums)
    print(cnt)
    print(max(cnt.keys(), key=cnt.get))
