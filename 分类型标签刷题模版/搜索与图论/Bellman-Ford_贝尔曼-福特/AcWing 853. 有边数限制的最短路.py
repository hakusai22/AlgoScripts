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
# @Time    : 2023/02/06 16:23

"""
    给定一个 n个点 m条边的有向图，图中可能存在重边和自环， 边权可能为负数。
    请你求出从 1号点到 n号点的最多经过 k条边的最短距离，如果无法从 1号点走到 n号点，输出 impossible。
    图中可能 存在负权回路 。
    
    数据范围
        1≤n,k≤500
        1≤m≤10000
        1≤x,y≤n
        任意边长的绝对值不超过 10000
        
    1)初始化所有点到源点的距离为∞,把源点到自己的距离设置为0；
    2)遍历n次;每次遍历m条边，用每一条边去更新各点到源点的距离。
        
    bellman - ford算法擅长解决有边数限制的最短路问题
    for n次
        for 所有边 a,b,w (松弛操作)
            dist[b] = min(dist[b],back[a] + w)
            
            算法步骤
                0.初始化dist数组为正无穷，dist[1]=0;
                1.（外重循环）循环i从1到n，遍历n次指的：是不经过i条边到达终点的最短距离 经过n次操作n个点的最短距离也就确定了；
                2.（内重循环）循环j从1到m，遍历m条边，把所有边都进行松弛操作
                每次取出两点以及他们连接的边的权重（a,b,w表示a—>b的一条边）
                用从起点到a的当前最短距离+权重来更新从起点到b的当前最短距离
                dist[b]=min(dist[b],dist[a]+w);
                3.返回答案
"""

N = 510
M = 10010
dist = [0x3f3f3f3f] * N # dist[N]表示从起点到当前点的当前最短距离
edge = [[0, 0, 0] for _ in range(M)]

def bellman_ford():
    dist[1] = 0
    for i in range(k): #枚举k次
        # back[] 数组是上一次迭代后 dist[] 数组的备份，由于是每个点同时向外出发，
        # 因此需要对 dist[] 数组进行备份，若不进行备份会因此发生串联效应，影响到下一个点
        backup = dist.copy()
        for j in range(m):
            a, b, c = edge[j]
            dist[b] = min(dist[b], backup[a] + c)

    return dist[n]

n, m, k = map(int, input().split())
for i in range(m):
    a, b, c = map(int, input().split())
    edge[i] = [a, b, c]

t = bellman_ford()
if t > 0x3f3f3f3f / 2:
    print("impossible")
else:
    print(t)
