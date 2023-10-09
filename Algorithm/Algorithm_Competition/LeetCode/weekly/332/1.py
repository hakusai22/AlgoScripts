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

# -*- coding: utf-8 -*-
# @Author  : wheat
# @Time    : 2023/02/12 11:31

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        res1 = 0
        while i < j:
            res = int(str(nums[i]) + str(nums[j]))
            res1 += res
            i += 1
            j -= 1

        if i == j:
            res1 += nums[i]
        return res1
