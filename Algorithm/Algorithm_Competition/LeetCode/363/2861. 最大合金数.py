from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache
from typing import List, Optional
import sys

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


# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2023/09/18 22:42

class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int,
                          composition: List[List[int]], stock: List[int],
                          cost: List[int]) -> int:

        ans = 0
        for com in composition:
            def check(num: int) -> int:
                m = 0
                for s, base, c in zip(stock, com, cost):
                    if s < base * num:
                        m += (base * num - s) * c
                        if m > budget:
                            return False
                return True

            l, r = 0, 10 ** 9
            while l + 1 < r:
                mid = (l + r) // 2
                if check(mid):
                    l = mid
                else:
                    r = mid
            ans = max(ans, l)
        return ans
