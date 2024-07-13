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
# @Time    : 2023/09/19 08:36
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def slove(mx: int) -> int:
            cur = pre = 0
            for x in nums:
                if x > mx:
                    pre = cur
                else:
                    pre, cur = cur, max(cur, pre + 1)
            return cur

        return bisect_left(range(max(nums)), k, key=slove)


if __name__ == '__main__':
    print(Solution.minCapability(self=None, nums=[2, 3, 5, 9], k=2))
