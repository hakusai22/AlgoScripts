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
# @Time    : 2023/02/02 15:00

"""
    一个正整数 n 可以表示成若干个正整数之和，形如：n=n1+n2+…+nk ，其中 n1≥n2≥…≥nk,k≥1。
    我们将这样的一种表示称为正整数 n 的一种划分。
    现在给定一个正整数 n，请你求出 n 共有多少种不同的划分方法。

    f[i][j]表示所有总和是i，并且恰好表示成j个数的和的方案的数量
    此时集合的划分是：
        1.该方案中最小值是1  方案数等于舍弃该1后的方案数，因此此时的方案数是：f[i−1][j−1]
        2.该方案中最小值大于1 把每一个数都减去1后每一个数仍大于等于1，仍合法，因此此时方案数等于把当前每个数减1的方案数，即：f[i−j][j]
    状态转移方程：
        f[i][j]=f[i−1][j−1]+f[i−j][j];
"""

if __name__ == '__main__':
    N = 1010
    mod = 1e9 + 7
    f = [[0] * N for _ in range(N)]

    # 表示总和为0，恰好是0个数的和的方案，也就是1.
    f[0][0] = 1
    n = int(input())

    for i in range(1, n + 1):
        for j in range(1, i + 1):  # 最多只有i个数，因为最小值是1，所以j最大只能取到i
            f[i][j] = (f[i - 1][j - 1] + f[i - j][j]) % mod

    res = 0
    for i in range(1, n + 1):
        res = (res + f[n][i]) % mod
    print(int(res))
