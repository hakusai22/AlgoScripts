# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/9/2 00:13


# 答案分为两部分：
# 所有垃圾的数目，即 garbage 中所有字符串的长度之和。
# 根据每一种字符在 garbage 中最后一次出现的下标，即每辆垃圾车必须向右开到的房子的最小值，得到每辆车需要开的最短距离。
#
from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = 0
        right = {}
        for i, s in enumerate(garbage):
            ans += len(s)
            for c in s:
                right[c] = i
        return ans + sum(sum(travel[:r]) for r in right.values())
