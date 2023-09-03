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
# @Time    : 2023/02/08 11:34

"""
    给定一个 n个点 m条边的有向图，图中可能存在重边和自环， 边权可能为负数。
    请你判断图中是否存在负权回路。
    输入格式
        第一行包含整数 n和 m
        接下来 m行每行包含三个整数 x,y,z，表示存在一条从点 x到点 y的有向边，边长为 z
    输出格式
        如果图中存在负权回路，则输出 Yes，否则输出 No。
    数据范围
        1≤n≤2000
        1≤m≤10000
    图中涉及边长绝对值均不超过 10000
    
    用n表示图中顶点数目，用m表示图中边或弧的数目（若图中边或弧上有权，则该图称为网）
    稀疏图: m < nlogn 邻接表存储
    稠密图: m > nlogn 邻接矩阵存储
    
    方法 1：统计每个点入队的次数，如果某个点入队n次，则说明存在负环
    方法 2：统计当前每个点的最短路中所包含的边数，如果某点的最短路所包含的边数大于等于n，则也说明存在环
"""

N = 2010
M = 10010
h = [-1] * N
e = [0] * M
ne = [0] * M
idx = 0
st = [True] * N
dist = [0] * N # 记录虚拟源点到x的最短距离
cnt = [0] * N # //从虚拟点到x经过的边数
w = [0] * M

def add(a, b, c):
    global idx
    e[idx] = b
    w[idx] = c
    ne[idx] = h[a]
    h[a] = idx
    idx += 1

def spfa():
    dist[1] = 0
    q = list(range(1, n + 1))
    hh, tt = 0, n - 1
    while hh <= tt:
        t = q[hh]
        hh += 1
        st[t] = False
        i = h[t]
        while i != -1:
            j = e[i]
            if dist[j] > dist[t] + w[i]:
                dist[j] = dist[t] + w[i]
                cnt[j] = cnt[t] + 1
                if cnt[j] >= n:
                    return True
                if not st[j]:
                    q.append(j)
                    tt += 1
                    st[j] = True

            i = ne[i]
    return False

n, m = map(int, input().split())
while m:
    m -= 1
    a, b, c = map(int, input().split())
    add(a, b, c)

if spfa():
    print("Yes")
else:
    print("No")
