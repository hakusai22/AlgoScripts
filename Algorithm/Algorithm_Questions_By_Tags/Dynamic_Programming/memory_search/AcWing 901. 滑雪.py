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
# @Time    : 2023/02/03 17:14

"""
    给定一个 R行 C列的矩阵，表示一个矩形网格滑雪场。
    矩阵中第 i行第 j列的点表示滑雪场的第 i行第 j列区域的高度。
    一个人从滑雪场中的某个区域内出发，每次可以向上下左右任意一个方向滑动一个单位距离。
    当然，一个人能够滑动到某相邻区域的前提是该区域的高度低于自己目前所在区域的高度。
    // 25出发 从高到低转圈 1结束 经过25个点
    1  2  3  4  5
    16 17 18 19 6
    15 24 25 20 7
    14 23 22 21 8
    13 12 11 10 9
    
    使用记忆化数组 记录每个点的最大滑动长度
    遍历每个点作为起点
    然后检测该点四周的点 如果可以滑动到其他的点
    那么该点的最大滑动长度 就是其他可以滑到的点的滑动长度+1
    dp[i][j] = max(dp[i][j-1], dp[i][j+1],dp[i-1][j],dp[i+1][j])

    由于滑雪是必须滑到比当前低的点 所以不会存在一个点多次进入的问题
    如果该点的dp[][] 不为初始化值 那么就说明计算过 不必再次计算。
"""

N = 310
f = [[-1] * N for _ in range(N)]
g = [[0] * N for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dp(x, y):
    if f[x][y] != -1:
        return f[x][y]

    f[x][y] = 1
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if 1 <= a <= n and 1 <= b <= m and g[a][b] < g[x][y]:
            f[x][y] = max(f[x][y], dp(a, b) + 1)

    return f[x][y]

if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(1, n + 1):
        g[i] = [0] + list(map(int, input().split()))
    res = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            res = max(res, dp(i, j))
    print(res)
