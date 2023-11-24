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
"""

if __name__ == '__main__':
    N = 510
    f = [[0] * N for _ in range(N)]

    n = int(input())
    for i in range(1, n + 1):
        f[i] = [0] + list(map(int, input().split()))

    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            f[i][j] = max(f[i + 1][j], f[i + 1][j + 1]) + f[i][j]

    print(f[1][1])
