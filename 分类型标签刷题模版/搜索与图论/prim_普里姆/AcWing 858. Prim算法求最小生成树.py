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
        1≤n≤500
        1≤m≤10^5
        稠密图
        
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

N = 510
INF = 0x3f3f3f3f
st = [False] * N  # 节点是否被加入到生成树中
dist = [INF] * N  # 存储各个节点到生成树的距离
g = [[INF] * N for _ in range(N)]  # 存储图

def prim():
    res = 0
    # 每次循环选出一个点加入到生成树
    for i in range(n):
        t = -1
        # 每个节点一次判断
        for j in range(1, n + 1):
            # 如果没有在树中，且到树的距离最短，则选择该点
            if not st[j] and (t == -1 or dist[t] > dist[j]):
                t = j

        # 如果孤立点，直返输出不能，然后退出
        if i and dist[t] == INF:
            return INF

        # 选择该点
        if i:
            res += dist[t]

        # 更新生成树外的点到生成树的距离
        for j in range(1, n + 1):
            # 从 t 到节点 j 的距离小于原来距离，则更新
            dist[j] = min(dist[j], g[t][j])

        st[t] = True

    return res

if __name__ == '__main__':
    n, m = map(int, input().split())  # n 个节点，m 条边
    while m:
        m -= 1
        a, b, c = map(int, input().split())
        g[a][b] = min(g[a][b], c)
        g[b][a] = g[a][b]

    t = prim()
    if t == INF:
        print("impossible")
    else:
        print(t)
