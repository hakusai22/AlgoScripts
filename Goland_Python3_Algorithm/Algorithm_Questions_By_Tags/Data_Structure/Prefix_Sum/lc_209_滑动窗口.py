# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/8 20:22
from typing import List


def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    i = 0
    sum = 0
    res = len(nums) + 1
    for j in range(len(nums)):
        sum += nums[j]
        while sum >= target:
            res = min(res, j + 1 - i)
            sum -= nums[i]
            i += 1
    return 0 if res > len(nums) else res
