from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby, pairwise
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, cache
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

# --idea
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2023/10/06 15:53
#
# 给你一个整数数组 prices 和一个整数 k ，其中 prices[i] 是某支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        # 记忆化搜索 dfs(i,j,k)，表示从第 i 天开始，最多完成 j 笔交易，
        # 以及当前持有股票的状态为 k（不持有股票用 0 表示，持有股票用 1 表示）时，所能获得的最大利润
        @cache
        def dfs(i, j, k):
            if i >= len(prices):
                return 0
            # 什么都不干
            ans = dfs(i + 1, j, k)
            # 拥有
            if k:
                # 卖出
                ans = max(ans, prices[i] + dfs(i + 1, j, 0))
            # 买入
            elif j:
                ans = max(ans, -prices[i] + dfs(i + 1, j - 1, 1))
            return ans

        return dfs(0, k, 0)
