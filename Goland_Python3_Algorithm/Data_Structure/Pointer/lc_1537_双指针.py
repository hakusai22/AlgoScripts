# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/23 09:12
import math
from typing import List


def maxSum(nums1: List[int], nums2: List[int]) -> int:
    sum1, sum2, i, j, INF = 0, 0, 0, 0, int(math.pow(10, 9) + 7)
    while i < len(nums1) and j < len(nums2):
        # 小的一方先走
        if nums1[i] < nums2[j]:
            sum1 += nums1[i]
            i += 1
        elif nums2[j] < nums1[i]:
            sum2 += nums2[j]
            j += 1
        else:
            # 遇到岔口，更新两个sum为最大值，同时取余
            sum1 = sum2 = (max(sum1, sum2) + nums1[i]) % INF
            i += 1
            j += 1
    # 加上数组中剩余的数字
    sum1, sum2 = sum1 + sum(nums1[i:]), sum2 + sum(nums2[j:])
    # 返回较大者取余的结果
    return max(sum1, sum2) % INF


if __name__ == '__main__':
    print(maxSum([2, 4, 5, 8, 10], [4, 6, 8, 9]))
