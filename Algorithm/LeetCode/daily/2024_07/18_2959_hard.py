from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby, pairwise
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, cache, reduce
from typing import List, Optional
import sys

from sortedcontainers import SortedList, SortedDict, SortedSet

sys.setrecursionlimit(10001000)

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')  # 负无穷
INFMAX = float('inf')  # 正无穷
PI = 3.141592653589793
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'

# @Author  : https://github.com/hakusai22
# @Time    : 2024/07/17 16:55
# @题目     : https://leetcode.cn/problems/number-of-possible-sets-of-closing-branches/?envType=daily-question&envId=2024-07-17
# @参考     :   https://leetcode.cn/problems/number-of-possible-sets-of-closing-branches/solutions/2560722/er-jin-zhi-mei-ju-floydgao-xiao-xie-fa-f-t7ou/?envType=daily-question&envId=2024-07-17
# 时间复杂度 : 二进制枚举 + Floyd

class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        g = [[inf] * n for _ in range(n)]
        for x, y, wt in roads:
            g[x][y] = min(g[x][y], wt)
            g[y][x] = min(g[y][x], wt)

        f = [None] * n

        def check(s):
            for i, row in enumerate(g):
                if s >> i & 1:
                    f[i] = row.copy()

            for k in range(n):
                if (s >> k & 1) == 0:
                    continue
                for i in range(n):
                    if (s >> i & 1) == 0 or f[i][k] == inf:
                        continue
                    for j in range(n):
                        f[i][j] = min(f[i][j], f[i][k] + f[k][j])

            for i, di in enumerate(f):
                if (s >> i & 1) == 0:
                    continue
                for j, dij in enumerate(di[:i]):
                    if s >> j & 1 and dij > maxDistance:
                        return 0
            return 1

        return sum(check(s) for s in range(1 << n))
