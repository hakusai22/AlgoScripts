# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/24 09:39
from typing import List

# https://leetcode.cn/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(nums: List[int], k: int) -> int:
        n = len(nums)
        ans = sumi = 0
        d = {0: 1}
        for i in range(n):
            sumi += nums[i]
            sumj = sumi - k  # 找另一半
            if sumj in d: ans += d[sumj]
            d[sumi] = d.get(sumi, 0) + 1  # 更新dict
        return ans


if __name__ == '__main__':
    print(Solution.subarraySum([1, 1, 1], 2))
