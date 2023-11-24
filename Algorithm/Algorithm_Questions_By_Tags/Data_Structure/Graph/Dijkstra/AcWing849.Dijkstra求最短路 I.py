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

"""
    给定一个 n个点 m条边的有向图，图中可能存在重边和自环，所有边权均为正值。
    请你求出 1号点到 n号点的最短距离，如果无法从 1号点走到 n号点，则输出 −1
    输出一个整数，表示 1号点到 n 号点的最短距离。
    数据范围
        1≤n≤500
        1≤m≤105
        图中涉及边长均不超过10000。
        
    Dijkstra.md 的整体思路比较清晰
        即进行n（n为n的个数）次迭代去确定每个点到起点的最小值 最后输出的终点的即为我们要找的最短路的距离
    
    朴素 Dijkstra。
        设 dist[1] = 0 和 dist[i] = INF。
        设集合 S为当前已确定最短路径的点。找出不在 S中且 dist 最小的点 t
        用 t更新所有点的距离。
    时间复杂度 O(n^2)
"""


if __name__ == '__main__':
    N = 510
    # 因为题目的边远大于点，因此是稠密图，稠密图用邻接矩阵去存。
    # 用于存储每个点到起点的最短距离
    d = [[0x3f3f3f3f] * N for _ in range(N)]
    # dist为每个点到起点的距离
    dist = [0x3f3f3f3f] * N
    # st表示每个点的最短距离已经确定了
    st = [False] * N

    def dijkstra():
        dist[1] = 0
        # 迭代 n - 1 次，因为每迭代一次，一个点的最短距离就确定了，并把它加入到确定的集合当中。
        # 前 n - 1 个点已经确定，那么最后一个点自然也就是最短距离了，所以可以把 n 改成 n - 1
        for i in range(n - 1):
            # 将t设置为-1 因为Dijkstra算法适用于不存在负权边的图
            t = -1
            # 循环每个点，找到最短距离的点，并把它赋值给 t
            for j in range(1, n + 1):
                # 该步骤即寻找还未确定最短路的点中路径最短的点
                if not st[j] and dist[j] < dist[t]:
                    t = j
            # 同时该点的最短路径也已经确定我们将该点标记
            st[t] = True
            # 根据该点更新其他所有点的距离
            for j in range(1, n + 1):
                dist[j] = min(dist[j], dist[t] + d[t][j])

            # 如果取到了最后一个点，则最后一个点的最短距离被找到，结束循环。
            if t == n:
                break

        if dist[n] == 0x3f3f3f3f:
            return -1
        return dist[n]

    n, m = map(int, input().split())
    while m:
        a, b, c = map(int, input().split())
        d[a][b] = min(d[a][b], c)
        m -= 1
    print(dijkstra())
