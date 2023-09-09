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


"""
    给定一个 n个点 m条边的有向图，图中可能存在重边和自环。
    所有边的长度都是 1，点的编号为 1∼n
    请你求出 1号点到 n号点的最短距离，如果从 1号点无法走到 n号点，输出 −1
    
    图的存储：邻接表
        用 h 数组保存各个节点能到的第一个节点的编号。开始时，h[i] 全部为 -1。
        用 e 数组保存节点编号，ne 数组保存 e 数组对应位置的下一个节点所在的索引。
        用 idx 保存下一个 e 数组中，可以放入节点位置的索引
        插入边使用的头插法，例如插入：a->b。首先把b节点存入e数组，e[idx] = b。然后 b 节点的后继是h[a]，ne[idx] = h[a]。最后，a 的后继更新为 b 节点的编号，h[a] = idx，索引指向下一个可以存储节点的位置，idx ++ 。

    从 1 号节点开始，广度优先遍历：
        1 号节点入队列，dist[1] 的值更新为 0。
        如果队列非空，就取出队头，找到队头节点能到的所有节点。如果队头节点能到走到的节点没有标记过，就将节点的dist值更新为队头的dist值+1，然后入队。
        重复步骤 2 直到队列为空。
        这个时候，dist数组中就存储了 1 号节点到各个节点的距离了。如果距离是无穷大，则不能到达，输出 -1，如果距离不是无穷大，则能到达，输出距离。

"""

# -*- coding: utf-8 -*-
# @Author  : wheat
# @Time    : 2023/02/06 13:40

def add(a, b):
    global idx
    e[idx] = b
    ne[idx] = h[a]
    h[a] = idx
    idx += 1

def bfs():
    deque.append(1)
    # 当我们的队列不为空时
    while deque:
        t = deque.popleft()
        i = h[t]
        # 遍历t节点的每一个邻边
        while i != -1:
            j = e[i]
            # 如果j没有被扩展过
            if d[j] == -1:
                # d[j]存储j节点离起点的距离，并标记为访问过
                d[j] = d[t] + 1
                # 把j结点 压入队列
                deque.append(j)
            i = ne[i]
    return d[-1]

if __name__ == "__main__":
    n, m = map(int, input().split())  # n个节点m条边
    idx = 0
    h = [-1] * (n + 1)
    ne = [0] * (m + 1)
    e = [0] * (m + 1)
    d = [-1] * (n + 1)  # 存储每个节点离起点的距离  d[1]=0
    d[1] = 0
    for _ in range(m):
        a, b = map(int, input().split())
        add(a, b)
    print("%d" % bfs())
