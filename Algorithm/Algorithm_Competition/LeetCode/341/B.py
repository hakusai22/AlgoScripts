
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
# @Author  : wink
# @Time    : 2023/04/16 10:09

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        scores = [0] * len(divisors)  # 初始化得分数组
        for i, d in enumerate(divisors):
            for n in nums:
                if n % d == 0:
                    scores[i] += 1  # 计算得分
        max_score = max(scores)  # 找到最大得分
        max_divisor = float('inf')
        for i, score in enumerate(scores):
            if score == max_score and divisors[i] < max_divisor:
                max_divisor = divisors[i]  # 找到得分最大的、数值最小的除数
        return max_divisor
