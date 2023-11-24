# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/9/21 23:36
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res


if __name__ == '__main__':
    res = Solution.permute(self=None, nums=[1, 2, 3])
    print(res)
