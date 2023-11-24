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
# @Time    : 2023/02/06 14:18

"""
    给定一个 n个点 m条边的有向图，点的编号是 1到 n，图中可能存在重边和自环。
    请输出任意一个该有向图的拓扑序列，如果拓扑序列不存在，则输出 −1
    若一个由图中所有点构成的序列 A满足：对于图中的每条边 (x,y)，x 在 A中都出现在 y之前，则称 A是该图的一个拓扑序列。
    
    如果存在拓扑序列，则输出任意一个合法的拓扑序列即可
    
    解题思路
        1.首先记录各个点的入度
        2.然后将入度为 0 的点放入队列
        3.将队列里的点依次出队列，然后找出所有出队列这个点发出的边，删除边，同事边的另一侧的点的入度 -1。
        4.如果所有点都进过队列，则可以拓扑排序，输出所有顶点。否则输出-1，代表不可以进行拓扑排序
    
"""

# 邻接表存储图
N = 100010
e = [0] * N
ne = [0] * N
h = [-1] * N
idx = 0
# 入队 队列保存入度为0的点，也就是能够输出的点
q = [0] * N
# 入度 保存各个点的入度
d = [0] * N

def add(a, b):
    global idx
    e[idx] = b
    ne[idx] = h[a]
    h[a] = idx
    idx += 1

def topsort():
    hh, tt = 0, -1
    # 由于入度的点是从1 ~ n，因此是从1 ~ n 遍历，如果有入度为0的点，则把它入队
    for i in range(1, n + 1):
        if not d[i]:
            tt += 1
            q[tt] = i

    # 循环处理队列中点的
    while hh <= tt:
        t = q[hh]
        hh += 1
        i = h[t]
        # 循环删除 t 发出的边
        while i != -1:
            # t 有一条边指向j
            j = e[i]
            # 删除边后，b的入度减1
            d[j] -= 1
            # 如果b的入度减为 0,则 b 可以输出，入队列
            if d[j] == 0:
                tt += 1
                q[tt] = j
            i = ne[i]
    # 如果队列中的点的个数与图中点的个数相同，则可以进行拓扑排序
    return tt == n - 1

n, m = map(int, input().split())

while m:
    m -= 1
    a, b = map(int, input().split())
    # 添加从a -> b 的一条边，b的入度 + 1
    add(a, b)
    d[b] += 1

if topsort():
    for i in range(n):
        print(q[i], end=" ")
else:
    print(-1)
