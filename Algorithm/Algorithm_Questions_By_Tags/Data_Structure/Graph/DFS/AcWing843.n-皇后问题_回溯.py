from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from typing import List, Tuple, Optional, Dict, Set
from collections import defaultdict, Counter, deque, OrderedDict, namedtuple
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, reduce
from copy import deepcopy

MOD = int(1e9 + 7)
INF = int(1e20)

"""
    n−皇后问题是指将 n个皇后放在 n×n的国际象棋棋盘上，使得皇后不能相互攻击到，
    即任意两个皇后都不能处于同一行、同一列或同一斜线上。
    现在给定整数 n，请你输出所有的满足条件的棋子摆法。
    
    // bool数组用来判断搜索的下一个位置是否可行
    // col列，dg对角线，udg反对角线
    // g[N][N]用来存路径
    
"""

if __name__ == '__main__':
    N = 20
    path = [[0] * N for _ in range(N)]
    col, dg, udg = [False] * N, [False] * N, [False] * N

    def dfs(u):
        if u == n:
            for i in range(n):
                for j in range(n):
                    print(path[i][j], end="")
                print()
            print()
            return

        # 枚举u这一行，搜索合法的列
        for j in range(n):
            if not col[j] and not dg[j + u] and not udg[u - j + n]:
                path[u][j] = 'Q'
                col[j], dg[j + u], udg[u - j + n] = True, True, True
                dfs(u + 1)
                col[j], dg[j + u], udg[u - j + n] = False, False, False
                path[u][j] = '.'

    n = int(input())
    for i in range(n):
        for j in range(n):
            path[i][j] = '.'

    dfs(0)
