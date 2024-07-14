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

# @Author  : https://github.com/hakusai22
# @Time    : 2024/07/14 21:49
# @题目     : https://leetcode.cn/problems/max-increase-to-keep-city-skyline/description/?envType=daily-question&envId=2024-07-14
# @参考     : https://leetcode.cn/problems/max-increase-to-keep-city-skyline/solutions/2842679/zeng-jia-dao-xing-lie-zui-da-zhi-pythonj-bvb8/?envType=daily-question&envId=2024-07-14
# 时间复杂度 : 时间复杂度：O(mn)，其中 m 和 n 分别为 grid 的行数和列数。

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = list(map(max, grid))
        col_max = list(map(max, zip(*grid)))
        ans = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                ans += min(row_max[i], col_max[j]) - x
        return ans
