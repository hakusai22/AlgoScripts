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
# @Time    : 2023/01/31 14:18

"""
    有 N 种物品和一个容量是 V 的背包，每种物品都有无限件可用。
    第 i 种物品的体积是 vi，价值是 wi。
    求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
    输出最大价值。
    状态转移方程：f[j] = max(f[j], f[j - v[i]] + w[i])
"""

if __name__ == '__main__':
    N = 1010
    v = [0] * N
    w = [0] * N
    f = [[0] * N for _ in range(N)]
    n, m = map(int, input().split())

    for i in range(1, n + 1):
        v[i], w[i] = map(int, input().split())

    for i in range(1, n + 1):
        # 和01背包问题的解法不一样，区别在于遍历体积 j时从逆序改为顺序
        # 在这里，因为每个物品可以取任意多次，所以不再强求用上一轮的状态，即本轮放过的物品，在后面还可以再放;
        for j in range(v[i], m + 1):
            f[j] = max(f[j], f[j - v[i]] + w[i])
    print(f[m])
