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
# @Time    : 2023/02/01 10:54

"""
    给定一个如下图所示的数字三角形，从顶部出发，
    在每一结点可以选择移动至其左下方的结点或移动至其右下方的结点，
    一直走到底层，要求找出一条路径，使路径上的数字的和最大。
                    7
                  3   8
                8   1   0
              2   7   4   4
            4   5   2   6   5
    一、状态表示：f[i][j]
        1. 集合：从顶点出发到第 i 行第 j 个数的最大路径和 
           每个点有两种选择: 由左上方走到该点 和 由右上方走到该点
        2. 属性：最大值
        f[i][j] = max(f[i - 1][j - 1], f[i - 1][j]) + a[i][j]
            
"""

if __name__ == '__main__':
    N = 510
    INF = -1e9
    a = [[INF] * N for _ in range(N)]
    f = [[INF] * N for _ in range(N)]
    n = int(input())
    for i in range(1, n + 1):
        a[i] = [INF] + list(map(int, input().split()))

    print(a)
    f[1][1] = a[1][1]
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            f[i][j] = max(f[i - 1][j - 1], f[i - 1][j]) + a[i][j]

    res = INF
    for i in range(1, n + 1):
        res = max(res, f[n][i])
    print(res)
