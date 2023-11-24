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

# 有向，稠密图
N = 210
graph = [[inf] * N for _ in range(N)]

def add(a, b, c):
    graph[a][b] = min(graph[a][b], c)

def Floyd():
    # 加入已知信息
    for i in range(1, n + 1):
        # 从自己到自己，最短路是0
        graph[i][i] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])  # 从第i节点到第j节点需要第k个节点

if __name__ == "__main__":
    n, m, query = map(int, input().split())
    for _ in range(m):
        a, b, c = map(int, input().split())
        add(a, b, c)

    Floyd()

    for _ in range(query):
        a, b = map(int, input().split())
        if graph[a][b] == inf:
            print("impossible")
        else:
            print(graph[a][b])
