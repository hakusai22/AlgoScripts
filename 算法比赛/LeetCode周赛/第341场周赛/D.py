from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache
import sys
from typing import List

sys.setrecursionlimit(10001000)

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')
INFMAX = float('inf')
PI = 3.141592653589793
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'

def alp(i):
    return chr(ord('a') + i % 26)  # i=0->'a', i=25->'z'

def input():
    return sys.stdin.readline().rstrip()

def end(r=-1):
    print(r)
    exit()

# -*- coding: utf-8 -*-
# @Author  : wink
# @Time    : 2023/04/16 11:04
class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        # 构建树的邻接表
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 标记需要减半价格的节点
        half_price = [False] * n
        for u in range(n):
            for v in adj[u]:
                if price[v] < price[u]:
                    half_price[u] = True
                    break

        # 减半价格
        for u in range(n):
            if half_price[u]:
                for v in adj[u]:
                    price[v] *= 0.5

        # 计算每次旅行的最小价格总和
        ans = 0
        for start, end in trips:
            q = deque([(start, 0)])
            visited = set()
            while q:
                u, cost = q.popleft()
                if u == end:
                    ans += cost
                    break
                visited.add(u)
                for v in adj[u]:
                    if v not in visited:
                        new_cost = cost + price[v]
                        if half_price[v]:
                            new_cost *= 0.5
                        q.append((v, new_cost))
        return int(ans)