
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/19 12:34
from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        price = defaultdict(lambda: defaultdict(int))
        for a, b, v in prices: price[a][b] = max(price[a][b], v)

        # 最多200*200
        @cache
        def solve(m, n):
            if m == 0 or n == 0: return 0
            ans = price[m][n]
            for i in range(1, m):
                ans = max(ans, solve(i, n) + solve(m - i, n))
            for i in range(1, n):
                ans = max(ans, solve(m, i) + solve(m, n - i))

            return ans

        return solve(m, n)