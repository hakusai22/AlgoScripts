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
# @Time    : 2023/01/31 15:29


"""
    有 N 种物品和一个容量是 V 的背包。
    第 i 种物品最多有 si件，每件体积是 vi，价值是 wi。
    求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
    输出最大价值。
    数据范围
        0<N,V≤100
        0<vi,wi,si≤100
    一、状态表示：f[i][j]
        1. 集合：从前i个物品中选,且总体积不超过j的所有方案的集合.
        2. 属性：最大值
        f[i][j] = max(f[i][j], f[i - 1][j - k * v[i]] + k * w[i]);
"""

if __name__ == '__main__':
    N = 110
    v = [0] * N
    w = [0] * N
    s = [0] * N
    f = [[0] * N for _ in range(N)]
    n, m = map(int, input().split())

    for i in range(1, n + 1):
        v[i], w[i], s[i] = map(int, input().split())

    # 枚举背包
    for i in range(1, n + 1):
        # 枚举体积
        for j in range(m + 1):
            # 枚举个数
            k = 0
            f[i][j] = f[i - 1][j]
            while 1:
                if k <= s[i] and k * v[i] <= j:
                    f[i][j] = max(f[i][j], f[i - 1][j - k * v[i]] + k * w[i])
                    k += 1
                else:
                    break
    print(f[n][m])
