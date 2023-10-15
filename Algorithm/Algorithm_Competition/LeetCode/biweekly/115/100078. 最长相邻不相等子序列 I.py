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


# --idea
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2023/10/15 16:19
class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str],
                                     groups: List[int]) -> List[str]:
        nums = [0]
        for v in range(1, n):
            if groups[v] != groups[v + 1]:
                nums.append(v)
        return [words[i] for i in nums]
