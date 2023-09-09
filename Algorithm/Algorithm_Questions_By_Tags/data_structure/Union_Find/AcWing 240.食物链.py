from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e, lcm
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from typing import List, Tuple, Optional, Dict, Set
from collections import defaultdict, Counter, deque, OrderedDict, namedtuple
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby, pairwise
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, reduce
from copy import deepcopy
from io import BytesIO, IOBase
import random
import sys
import os

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')
INFMAX = float('inf')


"""
   使用并查集记录每个节点到根节点的距离
     * a吃b 公式1  (dist[a]-1)%3==dist[b]%3 等价于 (dist[a]-1-dist[b])%3==0
     * a和b同类 公式2 dist[a]%3==dist[b]%3 等价于 (dist[a]-dist[b])%3==0
     * 
     * ①判断是否为同类  
     *      1.a和b已经合并  (dist[a]-dist[b])%3!=0 ans++
     *      2.a和b没有合并  把a的祖宗合并到b的祖宗上去  (dist[a]+dist[f1]-dist[b])%3==0
     *          dist[f1]=dist[b]-dist[a]
     * ② 判断a是否可以吃b
     *      1.a和b已经合并 (dist[a]-dist[b]-1)%3!=0  ans++
     *      2.a和b没有合并  (dist[a]+dist[f1]-1-dist[b])%3==0  
     *          dist[f1]=dist[b]-dist[a]+1
     *      // d[x] % 3 = 0 表示同类
            // d[x] % 3 = 1 表示x 可以吃根节点
            // d[x] % 3 = 2 表示x 被根节点吃
"""

if __name__ == '__main__':
    n, k = map(int, input().split())
    N = 50010
    p = [0 for i in range(N)]
    d = [0 for i in range(N)]
    for i in range(1, n + 1):
        p[i] = i

    # find函数，用于返回x的祖宗节点
    # 同时压缩往回搜寻节点的路径
    def find(x):
        if p[x] != x:
            t = find(p[x])
            d[x] += d[p[x]]
            p[x] = t
        return p[x]

    res = 0
    for i in range(k):
        t, x, y = MII()
        if x > n or y > n:
            res += 1
        else:
            px = find(x)
            py = find(y)
            if t == 1:
                if px == py and (d[x] - d[y]) % 3:
                    res += 1
                elif px != py:
                    p[px] = py
                    d[px] = d[y] - d[x]
            else:
                if px == py and (d[x] - d[y] - 1) % 3:
                    res += 1
                elif px != py:
                    p[px] = py
                    d[px] = d[y] + 1 - d[x]
    print(res)
