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
# https://leetcode.cn/contest/weekly-contest-338/problems/minimum-operations-to-make-all-array-elements-equal/

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums = sorted(nums)
        n = len(nums)
        pre_sum = [0]
        for t in nums:
            pre_sum.append(pre_sum[-1] + t)
        to_ret = []
        for t in queries:
            pt = bisect(nums, t + .1)
            part_1 = t * pt - pre_sum[pt]
            part_2 = (pre_sum[-1] - pre_sum[pt]) - t * (n - pt)
            to_ret.append(part_1 + part_2)

        return to_ret
