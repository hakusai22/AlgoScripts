from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache
import sys
from typing import List

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
# @Author  : wheat
# @Time    : 2023/04/03 14:36

def primeUpTo(n):
    primes = set(range(2, n + 1))
    for i in range(2, n):
        if i in primes:
            it = i * 2
            while it <= n:
                if it in primes:
                    primes.remove(it)
                it += i
    return primes

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        pls = list(primeUpTo(1000))
        pls.append(0)
        pls.append(10000)
        pls.sort()
        pres = 0
        for a in nums:
            a -= pres
            if a <= pls[0]:
                return False
            i = 0
            while i < len(pls) and a > pls[i + 1]:
                i += 1
            pres += a - pls[i]
        return True
