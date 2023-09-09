# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/8 20:31
import bisect
from typing import List


def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    if not nums: return 0
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    if nums[-1] < s: return 0
    res = float("inf")
    for i in range(len(nums)):
        if nums[i] - s >= 0:
            loc = bisect.bisect_left(nums, nums[i] - s)
            if nums[i] - nums[loc] == s:
                res = min(res, i - loc)
            else:
                res = min(res, i - loc + 1)
    return res
