from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from typing import List, Tuple, Optional, Dict, Set
from collections import defaultdict, Counter, deque, OrderedDict, namedtuple
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, reduce

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')
INFMAX = float('inf')

# -*- coding: utf-8 -*-
# @Author  : wheat
# @Time    : 2023/02/01 11:19

"""
给定一个长度为 N 的数列，求数值严格单调递增的子序列的长度最长是多少。
    数据范围
         1≤N≤100000，
        −109≤数列中的数≤109
    7
    3 1 2 1 8 5 6

    3 ----
    1 ----
    1 2 ----
    1 2 ----
    1 2 8 ----
    1 2 5 ----
    1 2 5 6 ----
    4

"""

if __name__ == '__main__':

    N = 100010
    # 存放所有不同长度下的上升子序列的结尾的最小值
    q = [0] * N

    n = int(input())
    a = list(map(int, input().split()))
    # 代表上升子序列的长度
    len = 0
    for i in range(n):
        l, r = 0, len
        while l < r:
            mid = l + r + 1 >> 1
            if q[mid] < a[i]:
                l = mid
            else:
                r = mid - 1
        # 更新(r+1)子序列长度的最小值为a[i]
        q[r + 1] = a[i]
        # 更新上升子序列的长度
        len = max(len, r + 1)

    print(len)
