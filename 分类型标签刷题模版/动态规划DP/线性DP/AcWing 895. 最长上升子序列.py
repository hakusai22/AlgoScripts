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
# @Time    : 2023/02/01 11:12

"""
给定一个长度为 N 的数列，求数值严格单调递增的子序列的长度最长是多少。
    
    状态表示：f[i]表示从第一个数字开始算，以w[i]结尾的最大的上升序列。
    (以w[i]结尾的所有上升序列中属性为最大值的那一个)
    状态计算（集合划分）：j∈(0,1,2,..,i-1), 
    在w[i] > w[j]时，f[i] = max(f[i], f[j] + 1)。
    有一个边界，若前面没有比i小的，f[i]为1（自己为结尾）。最后在找f[i]的最大值。
    
    数据范围
        1≤N≤1000，
        −109≤数列中的数≤109
"""

if __name__ == '__main__':
    N = 1010
    f = [1] * N
    n = int(input())
    a = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        for j in range(1, i):
            if a[i] > a[j]:
                f[i] = max(f[i], f[j] + 1)

    res = 0
    for i in range(1, n + 1):
        res = max(res, f[i])
    print(res)
