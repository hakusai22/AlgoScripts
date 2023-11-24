from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from typing import List, Tuple, Optional, Dict, Set
from collections import defaultdict, Counter, deque, OrderedDict, namedtuple
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, reduce
import sys
sys.setrecursionlimit(1000000)
MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')
INFMAX = float('inf')

# -*- coding: utf-8 -*-
# @Author  : wheat
# @Time    : 2023/02/03 16:49


"""
    Ural 大学有 N 名职员，编号为 1∼N
    他们的关系就像一棵以校长为根的树，父节点就是子节点的直接上司。
    每个职员有一个快乐指数，用整数 Hi给出，其中 1≤i≤N
    现在要召开一场周年庆宴会，不过，没有职员愿意和直接上司一起参会。
    在满足这个条件的前提下，主办方希望邀请一部分职员参会，使得所有参会职员的快乐指数总和最大，求这个最大值。
"""

if __name__ == '__main__':
    N = 6010
    hy = [0] * N
    h = [-1] * N
    e = [0] * N
    ne = [0] * N
    idx = 0
    f = [[0] * 2 for _ in range(N)]
    father = [False] * N

    def add(a, b):
        global idx
        e[idx] = b
        ne[idx] = h[a]
        h[a] = idx
        idx += 1

    def dfs(u):
        f[u][1] = hy[u]

        i = h[u]
        while i != -1:
            j = e[i]
            dfs(j)

            f[u][0] += max(f[j][0], f[j][1])
            f[u][1] += f[j][0]
            i = ne[i]

    n = int(input())
    for i in range(1, n + 1):
        hy[i] = int(input())

    for i in range(n - 1):
        a, b = map(int, input().split())
        father[a] = True
        add(b, a)

    root = 1
    while father[root]:
        root += 1

    dfs(root)

    print(max(f[root][0], f[root][1]))
