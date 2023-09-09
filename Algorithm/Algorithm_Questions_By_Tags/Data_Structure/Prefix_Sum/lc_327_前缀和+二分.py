# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/22 20:38
import bisect
from bisect import bisect_left, bisect_right
from typing import List


# 使用前缀数组pre，然后每个前缀和pre[i]二分查找前面i-1个和的pre[i]-lower和pre[i]-upper的位置得出区间和的数量，
# 然后把pre[i]二分插入到数组中保持数组有序
# https://leetcode.cn/problems/count-of-range-sum/


def countRangeSum(nums: List[int], lower: int, upper: int) -> int:
    n1 = len(nums)
    presum = [0 for _ in range(n1 + 1)]
    for i in range(n1):
        presum[i + 1] = presum[i] + nums[i]
    res = 0
    preWindow = []
    for i, p in enumerate(presum):
        L = bisect_left(preWindow, p - upper)
        R = bisect_right(preWindow, p - lower)
        res += (R - L)
        bisect.insort(preWindow, p)
    return res

if __name__ == '__main__':
    print(countRangeSum([-2, 5, -1], -2, 2))
