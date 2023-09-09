# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/24 09:29

# https://leetcode.cn/problems/product-of-array-except-self/
from typing import List


class Solution:
    def productExceptSelf(nums: List[int]) -> List[int]:
        n = len(nums)
        left_p = [1] * n  # nums[i]左侧数的乘积
        right_p = [1] * n  # nums[i]右侧数的乘积
        p = 1
        for i in range(1, n):
            p *= nums[i - 1]
            left_p[i] = p

        p = 1
        for i in range(n - 2, -1, -1):
            p *= nums[i + 1]
            right_p[i] = p

        ans = []
        # 除nums[i]以外的乘积 = nums[i]左侧数的乘积 * nums[i]右侧数的乘积
        for i in range(n):
            ans.append(left_p[i] * right_p[i])
        return ans


if __name__ == '__main__':
    print(Solution.productExceptSelf([1, 2, 3, 4]))
