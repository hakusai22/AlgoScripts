from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from typing import List, Tuple, Optional, Dict, Set
from collections import defaultdict, Counter, deque, OrderedDict, namedtuple
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, reduce
from copy import deepcopy


"""
    给定一个包含 n 个点（编号为 1∼n）的无向图，初始时图中没有边。
    现在要进行 m 个操作，操作共有三种：
        1. C a b，在点 a点 b之间连一条边，a和 b可能相等；
        2. Q1 a b，询问点 a和点 b是否在同一个连通块中，a和 b可能相等；
        3. Q2 a，询问点 a所在连通块中点的数量；
        
    对于每个询问指令 Q1 a b，如果 a 和 b 在同一个连通块中，则输出 Yes，否则输出 No。
    对于每个询问指令 Q2 a，输出一个整数表示点 a 所在连通块中点的数量
"""

if __name__ == '__main__':
    N = 100010
    p = [0] * N
    size = [0] * N

    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]

    n, m = map(int, input().split())

    for i in range(1, n + 1):
        p[i] = i
        size[i] = 1

    while m:
        m -= 1
        li = input().split()
        if li[0] == 'C':
            a, b = int(li[1]), int(li[2])
            if find(a) == find(b):
                continue
            size[find(b)] += size[find(a)]
            p[find(a)] = find(b)
        elif li[0] == 'Q1':
            a, b = int(li[1]), int(li[2])
            if find(a) == find(b):
                print("Yes")
            else:
                print("No")
        else:
            a = int(li[1])
            print(size[find(a)])

