# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/23 08:26
from typing import List


class Solution:
    def minNumberOfHours(self, eng: int, exp: int, energy: List[int], experience: List[int]) -> int:
        ans = 0
        # zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
        for x, y in zip(energy, experience):
            if eng <= x:
                ans += x + 1 - eng
                eng = x + 1  # 补到刚好超过
            eng -= x
            if exp <= y:
                ans += y + 1 - exp
                exp = y + 1  # 补到刚好超过
            exp += y
        return ans
