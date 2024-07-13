from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby, pairwise
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, cache, reduce
from typing import List, Optional
import sys

from sortedcontainers import SortedList, SortedDict, SortedSet

sys.setrecursionlimit(10001000)

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')  # 负无穷
INFMAX = float('inf')  # 正无穷
PI = 3.141592653589793
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'



def rep():
    a = list(map(int, input().split()))
    return a

def sep():
    a = input().rstrip('\n')
    return a

# --idea 
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2023/10/17 17:36

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def f(x):
            m = n // x
            return (x + m * x) * m // 2

        return f(3) + f(5) + f(7) - f(3 * 5) - f(3 * 7) - f(5 * 7) + f(3 * 5 * 7)
