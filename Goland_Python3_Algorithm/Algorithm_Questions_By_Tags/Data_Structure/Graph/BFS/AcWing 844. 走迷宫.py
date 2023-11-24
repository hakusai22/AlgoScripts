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
# @Time    : 2023/02/06 10:59


"""
    给定一个 n×m 的二维整数数组，用来表示一个迷宫，数组中只包含 0或 1 ，其中 0 表示可以走的路，1 表示不可通过的墙壁。
    最初，有一个人位于左上角 (1,1) 处，已知该人每次可以向上、下、左、右任意一个方向移动一个位置。
    请问，该人从左上角移动至右下角 (n,m)处，至少需要移动多少次。
    数据保证 (1,1) 处和 (n,m) 处的数字为 0 ，且一定至少存在一条通路。
    
    输出一个整数，表示从左上角移动至右下角的最少移动次数。
    
    广度优先遍历。
    思路：从起点开始，往前走第一步，记录下所有第一步能走到的点，然后从所第一步能走到的点开始，
    往前走第二步，记录下所有第二步能走到的点，重复下去，直到走到终点。输出步数即可。
"""

N = 110
g = [[0] * N for _ in range(N)]
d = [[-1] * N for _ in range(N)]
queue = [(0, 0)]

def bfs():
    d[0][0] = 0
    hh, tt = 0, 0
    x, y = [-1, 0, 1, 0], [0, 1, 0, -1]
    while hh <= tt:
        t = queue.pop(0)
        hh += 1
        for i in range(4):
            new_x, new_y = t[0] + x[i], t[1] + y[i]
            if 0 <= new_x < n and 0 <= new_y < m and g[new_x][new_y] == 0 and d[new_x][new_y] == -1:
                d[new_x][new_y] = d[t[0]][t[1]] + 1
                tt += 1
                queue.append((new_x, new_y))

    return d[n - 1][m - 1]

n, m = map(int, input().split())
for i in range(n):
    g[i] = list(map(int, input().split()))

print(bfs())
