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
# @Time    : 2023/02/06 16:06

"""
    给定一个 n个点 m条边的有向图，图中可能存在重边和自环，所有边权均为非负值。
    请你求出 1号点到 n号点的最短距离，如果无法从 1号点走到 n号点，则输出 −1
    输出一个整数，表示 1号点到 n 号点的最短距离。
    数据范围
        1≤n,m≤1.5×10^5,
        图中涉及边长均不小于 0，且不超过 10000。
        数据保证：如果最短路存在，则最短路的长度不超过 10^9
        
    堆优化的Dijkstra算法
        原先的Dijkstra算法主要针对稠密图，但如果是稀疏图，O(n^2)是会使得内存爆炸
        堆优化版的dijkstra是对朴素版dijkstra进行了优化，在朴素版dijkstra中时间复杂度最高的寻找距离
        最短的点O(n^2)可以使用最小堆优化。
            1. 一号点的距离初始化为零，其他点初始化成无穷大。
            2. 将一号点放入堆中。
            3. 不断循环，直到堆空。每一次循环中执行的操作为：
                弹出堆顶（与朴素版Dijkstra找到S外距离最短的点相同，并标记该点的最短路径已经确定）。
                用该点更新临界点的距离，若更新成功就加入到堆中。
"""

N = 150010
h = [-1] * N
ne = [0] * N
e = [0] * N
w = [0] * N
idx = 0
st = [False] * N
dist = [0x3f3f3f3f] * N

# 稀疏图用邻接表来存
def add(a, b, c):
    global idx
    e[idx] = b
    w[idx] = c
    ne[idx] = h[a]
    h[a] = idx
    idx += 1

def dijkstra_heap():
    dist[1] = 0
    heap = []
    heappush(heap, (0, 1))
    while heap:
        d, node = heappop(heap)
        if st[node]:
            continue
        st[node] = True
        i = h[node]
        while i != -1:
            j = e[i]
            if dist[j] > d + w[i]:
                dist[j] = d + w[i]
                heappush(heap, (dist[j], j))

            i = ne[i]

    if dist[n] == 0x3f3f3f3f:
        return -1
    return dist[n]

n, m = map(int, input().split())
while m:
    m -= 1
    a, b, c = map(int, input().split())
    add(a, b, c)

print(dijkstra_heap())
