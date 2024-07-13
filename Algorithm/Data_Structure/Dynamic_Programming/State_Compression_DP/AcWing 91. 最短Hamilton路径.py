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
# @Time    : 2023/02/03 16:04

"""
    给定一张 n 个点的带权无向图，点从 0∼n−1 标号，求起点 0 到终点 n−1 的最短 Hamilton 路径。
    Hamilton 路径的定义是从 0 到 n−1 不重不漏地经过每个点恰好一次。
    
    数据范围
     1≤n≤20
     0≤a[i,j]≤107
    
        用二进制来表示要走的所以情况的路径,这里用i来代替
        例如走0,1,2,4这三个点,则表示为:10111; 走0,2,3这三个点:1101;
        状态表示:f[i][j];
            集合:所有从0走到j,走过的所有点的情况是i的所有路径
            属性:MIN
            状态计算:如1中分析一致,0–>·····–>k–>j中k的所有情况
            状态转移方程:f[i][j]=min(f[i][j],f[i-(1<<j)][k]+w[k][j])
"""

if __name__ == '__main__':
    n = eval(input())
    weight = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0x3f3f3f3f] * n for _ in range(1 << n)]
    dp[1][0] = 0

    for i in range(1 << n):
        for j in range(n):
            if i >> j & 1:
                for k in range(n):
                    if i - (1 << j) >> k & 1:
                        dp[i][j] = min(dp[i][j], dp[i - (1 << j)][k] + weight[k][j])
    print(dp[(1 << n) - 1][n - 1])
