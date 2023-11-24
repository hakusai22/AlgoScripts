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
# @Time    : 2023/02/08 11:35

"""
    给定一个 n个点 m条边的无向图，图中可能存在重边和自环，边权可能为负数。
    求最小生成树的树边权重之和，如果最小生成树不存在则输出 impossible。
    给定一张边带权的无向图 G=(V,E)，其中 V表示图中点的集合，E表示图中边的集合，n=|V|，m=|E|
    由 V中的全部 n个顶点和 E中 n−1条边构成的无向连通子图被称为 G的一棵生成树，其中边的权值之和最小的生成树被称为无向图 G的最小生成树。
    若存在最小生成树，则输出一个整数，表示最小生成树的树边权重之和

    每次将离连通部分的最近的点和点对应的边加入的连通部分，连通部分逐渐扩大，最后将整个图连通起来，并且边长之和最小。
    时间复杂度为 O(n^2)。

    数据范围:
        1≤n≤10^5
        1≤m≤2*10^5
        稀疏图
        
        用n表示图中顶点数目，用e表示图中边或弧的数目（若图中边或弧上有权，则该图称为网）
        稀疏图: e < nlogn 邻接表存储
        稠密图: e > nlogn 邻接矩阵存储

    4 5
    1 2 1
    1 3 2
    1 4 3
    2 3 2
    3 4 4

    6
"""

N = 100010
M = 2 * N
p = [0] * N
edge = []

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

n, m = map(int, input().split())
for i in range(m):
    a, b, c = map(int, input().split())
    edge.append([a, b, c])

edge.sort(key=lambda x: x[2])

for i in range(1, n + 1):
    p[i] = i

res, cnt = 0, 0
for i in range(m):
    a, b, w = edge[i]
    a = find(a)
    b = find(b)
    # 当 a == b 的时候，就代表形成了环。因此丢弃该边，进行下一个边
    if a != b:
        p[a] = b
        res += w
        cnt += 1

if cnt == n - 1:
    print(res)
else:
    print("impossible")
