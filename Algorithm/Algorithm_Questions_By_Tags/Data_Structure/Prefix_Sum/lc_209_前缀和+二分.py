# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/24 09:11
from bisect import bisect_left
from typing import List


# https://leetcode.cn/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(s: int, nums: List[int]) -> int:
        if not nums: return 0
        # 求前缀和
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        # 总和都小于 s 时候
        if nums[-1] < s: return 0
        res = float("inf")
        nums = [0] + nums
        for i in range(1, len(nums)):
            if nums[i] - s >= 0:
                # 二分查找 找到大于等于nums[i] - s的第一个数
                loc = bisect_left(nums, nums[i] - s)
                if nums[i] - nums[loc] >= s:
                    res = min(res, i - loc)
                    continue
                if loc > 0:
                    res = min(res, i - loc + 1)
        return res


if __name__ == '__main__':
    print(Solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
