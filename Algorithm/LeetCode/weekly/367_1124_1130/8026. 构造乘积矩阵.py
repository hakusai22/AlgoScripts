from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby, pairwise
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, cache
from typing import List, Optional
import sys

from sortedcontainers import SortedList, SortedDict, SortedSet

sys.setrecursionlimit(10001000)

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')
INFMAX = float('inf')
PI = 3.141592653589793
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'


def alp(i):
    return chr(ord('a') + i % 26)  # i=0->'a', i=25->'z'


def input():
    return sys.stdin.readline().rstrip()


def end(r=-1):
    print(r)
    exit()


# --idea  把矩阵想象成一维的，我们需要算出每个数左边所有数的乘积，以及右边所有数的乘积
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2023/10/15 17:08

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        p = [[0] * m for _ in range(n)]
        suf = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = suf
                suf = suf * grid[i][j] % MOD

        pre = 1
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                p[i][j] = p[i][j] * pre % MOD
                pre = pre * x % MOD
        return p
