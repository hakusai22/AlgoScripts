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
    给定一个 n 个点 m 条边的有向图，图中可能存在重边和自环， 边权可能为负数。
    请你求出 1号点到 n号点的最短距离，如果无法从 1号点走到 n号点，则输出 impossible。
    数据保证不存在负权回路。
    输出一个整数，表示 1 号点到 n 号点的最短距离。
    
    数据范围
        1≤n,m≤105,
        图中涉及边长绝对值均不超过 10000。
        
        用n表示图中顶点数目，用m表示图中边或弧的数目（若图中边或弧上有权，则该图称为网）
        稀疏图: m < nlogn 邻接表存储
        稠密图: m > nlogn 邻接矩阵存储
        
    Bellman_ford算法会遍历所有的边，但是有很多的边遍历了其实没有什么意义，
    我们只用遍历那些到源点距离变小的点所连接的边即可，只有当一个点的前驱结点更新了，
    该节点才会得到更新；我们将创建一个队列每一次加入距离被更新的结点。
    
    要想松弛后面的点，必须要更新过当前的点，如果这个点都没有更新过，那么更新后面的点也是无效的
     适用范围：只要没有负环，都可以使用。
        spfa也能解决权值为正的图的最短距离问题，且一般情况下比Dijkstra算法还好

     时间复杂度：一般情况 O(m)
     1. 初始化dist[1]=0; dist[其他点] = 正无穷
     2. 队列不空
        1. 只有这个点被更新后，其他与它相连的点才会被更新
"""

N = 100010
h = [-1] * N
e = [0] * N
ne = [0] * N
idx = 0
st = [False] * N  # 判断当前的点是否已经加入到队列当中了
dist = [0x3f3f3f3f] * N
w = [0] * N

def add(a, b, c):
    global idx
    e[idx] = b
    w[idx] = c
    ne[idx] = h[a]
    h[a] = idx
    idx += 1

def spfa():
    dist[1] = 0
    q = Queue()
    q.put(1)
    st[1] = True
    while q.qsize():
        t = q.get()
        st[t] = False
        i = h[t]
        while i != -1:
            j = e[i]
            if dist[j] > dist[t] + w[i]:
                dist[j] = dist[t] + w[i]
                if not st[j]:
                    q.put(j)
                    st[j] = True

            i = ne[i]

    return dist[n]

n, m = map(int, input().split())
while m:
    m -= 1
    a, b, c = map(int, input().split())
    add(a, b, c)

t = spfa()
if t > 0x3f3f3f3f / 2:
    print("impossible")
else:
    print(t)
