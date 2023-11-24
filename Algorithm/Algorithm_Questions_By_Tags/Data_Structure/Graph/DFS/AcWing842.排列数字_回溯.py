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
    给定一个整数 n，将数字 1∼n排成一排，将会有很多种排列方法。
    现在，请你按照字典序将所有的排列方法输出。
"""

N = 10
path = [0] * N
st = [False] * N

def dfs(u):
    if u == n:
        for i in range(n):
            print(path[i], end=" ")
        print()
        return
    for i in range(1, n + 1):
        if not st[i]:
            path[u] = i
            st[i] = True
            dfs(u + 1)
            st[i] = False

if __name__ == '__main__':

    n = int(input())
    dfs(0)
