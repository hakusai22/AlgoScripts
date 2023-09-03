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
# @Time    : 2023/02/01 11:53

"""
给定两个长度分别为 N 和 M 的字符串A和B，求既是A的子序列又是B的子序列的字符串长度最长是多少。

    一、状态表示：f[i][j]
        集合：所有在A[1…i]中出现过且在B[1…j]中也出现过的子序列
        属性：Max
        如果两个字符相等，就可以直接转移到f[i-1][j-1] 
        否则 两个字符一定有一个可以抛弃，可以对f[i-1][j],f[i][j-1]两种状态取max来转移
        f[i][j] = f[i - 1][j - 1] + 1
"""

if __name__ == '__main__':
    N = 1010
    f = [[0] * N for _ in range(N)]

    n, m = map(int, input().split())
    a = " " + input()
    b = " " + input()

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            f[i][j] = max(f[i - 1][j], f[i][j - 1])
            if a[i] == b[j]:
                f[i][j] = f[i - 1][j - 1] + 1

    print(f[n][m])
