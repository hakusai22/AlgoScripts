# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/22 23:22
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        d = {}
        for n in nums:
            s = str(n)
            s_ = s[::-1]
            n_ = int(s_)
            k = n - n_
            d[k] = d.get(k, 0) + 1
        r = 0
        for k in d:
            r += d[k] * (d[k] - 1) // 2
            r %= mod
        return r
