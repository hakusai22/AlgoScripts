# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/9/21 23:45
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        temp = []

        def back(nums, temp):
            if not nums:
                res.append(temp)
                return
            else:
                for i in range(len(nums)):
                    if i > 0 and nums[i] == nums[i - 1]:
                        continue
                    back(nums[:i] + nums[i + 1:], temp + [nums[i]])  # 这种拼接方法是天然的标记，判断前一字符是否在循环里。

        back(nums, temp)
        return res
