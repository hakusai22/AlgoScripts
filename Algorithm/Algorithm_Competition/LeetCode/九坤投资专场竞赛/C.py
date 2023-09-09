# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/22 23:31
from typing import List


class Solution:
    def minOperations(self, numbers: List[int]) -> int:
        base = 0
        two = []
        three = []
        for num in numbers:
            tw = 0
            while num % 2 == 0:
                num //= 2
                tw += 1
            th = 0
            while num % 3 == 0:
                # //”，在python中，这个叫“地板除”，3//2=1
                num //= 3
                th += 1
            if base == 0:
                base = num
            elif base != num:
                return -1
            two.append(tw)
            three.append(th)
        hi2 = max(two)
        hi3 = max(three)
        n = len(numbers)
        return hi2 * n - sum(two) + hi3 * n - sum(three)
