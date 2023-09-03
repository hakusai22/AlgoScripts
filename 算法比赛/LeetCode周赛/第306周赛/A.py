# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/9/3 21:48
from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for i in range(n - 2):
            for j in range(n - 2):
                grid[i][j] = max(max(row[j:j + 3]) for row in grid[i:i + 3])
            del grid[i][-2:]
        del grid[-2:]
        return grid
