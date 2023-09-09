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
# @Time    : 2023/02/02 14:36

"""
    题意：合并 N 堆石子，每次只能合并相邻的两堆石子，求最小代价
    关键点：最后一次合并一定是左边连续的一部分和右边连续的一部分进行合并

    状态表示：f[i][j] 表示将 i 到 j 这一段石子合并成一堆的方案的集合，
    属性 Min
    前缀和数组 a[i]=a[i−1]+x[i] x[i-j]=a[j]−a[i−1]
    状态转移方程式:
        f[i][j]=min(f[i][j],f[i][k]+f[k+1][j]+a[j]−a[i−1])
    枚举顺序：
        很明显，长的区间由短的区间合并而成
        所以先枚举区间长度 len 接着枚举左端点 l(右端点由左端点和区间长度去确定)
        最后枚举分段点 k，计算 dp 方程
"""

if __name__ == '__main__':
    N = 310
    f = [[0] * N for _ in range(N)]
    s = [0] * N

    n = int(input())
    a = [0] + list(map(int, input().split()))

    for i in range(1, n + 1):
        s[i] = s[i - 1] + a[i]

    for len in range(2, n + 1):
        i = 1
        while i + len - 1 <= n:
            l = i
            r = i + len - 1
            f[l][r] = 1e9
            for k in range(l, r):
                f[l][r] = min(f[l][r], f[l][k] + f[k + 1][r] + s[r] - s[l - 1])
            i += 1

    print(f[1][n])
