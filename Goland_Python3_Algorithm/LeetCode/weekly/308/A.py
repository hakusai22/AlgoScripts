# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/9/1 23:30
# Prefix_Suffix + 二分解决。
from bisect import bisect_right
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        # Prefix_Suffix
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        # 二分找出第一个小于等于q的位置
        for i, q in enumerate(queries):
            queries[i] = bisect_right(nums, q)
        return queries
