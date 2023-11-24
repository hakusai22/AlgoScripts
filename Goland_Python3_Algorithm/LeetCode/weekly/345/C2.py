'''
Author: hakusai
Date: 2023-05-14 12:31:10
LastEditTime: 2023-05-14 12:40:34
'''
from collections import Counter, defaultdict, deque
from functools import lru_cache, reduce, cmp_to_key
from itertools import accumulate, combinations, permutations, product
from heapq import nsmallest, nlargest, heapify, heappop, heappush
from bisect import bisect_left, bisect_right
from math import factorial, gcd
from cmath import inf
from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        @lru_cache
        def dfs(i, j):
            ans = 0
            for dx, dy in ((i - 1, j + 1), (i, j+1), (i + 1, j + 1)):
                if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] > grid[i][j]:
                    ans = max(ans, dfs(dx, dy) + 1)
            return ans
        return max(dfs(i, 0) for i in range(m))
