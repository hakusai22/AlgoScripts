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
# @Time    : 2024/07/18 22:31
# @题目     : https://leetcode.cn/problems/minimum-time-to-visit-disappearing-nodes/description/?envType=daily-question&envId=2024-07-18
# @参考     :   https://leetcode.cn/problems/minimum-time-to-visit-disappearing-nodes/solutions/2738888/dijkstra-suan-fa-pythonjavacgo-by-endles-7q6u/?envType=daily-question&envId=2024-07-18
# 时间复杂度 :

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        g = [[] for _ in range(n)]  # 稀疏图用邻接表
        for x, y, wt in edges:
            g[x].append((y, wt))
            g[y].append((x, wt))

        dis = [-1] * n
        dis[0] = 0
        h = [(0, 0)]
        while h:
            dx, x = heappop(h)
            if dx > dis[x]:
                continue

            for y, wt in g[x]:
                new_dis = dx + wt
                if new_dis < disappear[y] and (dis[y] < 0 or new_dis < dis[y]):
                    dis[y] = new_dis
                    heappush(h, (new_dis, y))
        return dis
