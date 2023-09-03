'''
Author: hakusai
Date: 2023-05-14 12:12:15
LastEditTime: 2023-05-14 12:25:10
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
        # python要手动取反模拟大根堆
        m = len(grid)
        n = len(grid[0])
        q = [(grid[i][0], 0, i, 0) for i in range(m)]
        heapify(q)
        visit = [[False]*n for _ in range(m)]
        ans = 0
        while q:
            t, step, x, y = heappop(q)
            if visit[x][y]:
                continue
            ans = max(ans, -step)
            visit[x][y] = True
            for dx, dy in ((x - 1, y + 1), (x, y+1), (x + 1, y + 1)):
                if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] > t:
                    heappush(q, (grid[dx][dy], step - 1, dx, dy))
        return ans


if __name__ == "__main__":
    print(Solution.maxMoves(self=None, grid=[[2, 4, 3, 5], [
        5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]))
