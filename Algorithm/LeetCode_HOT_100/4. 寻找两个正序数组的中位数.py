# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/15 21:34
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = nums1[:] + nums2[:]
        x.sort()
        n = len(x)
        if n == 1:
            return x[0]
        else:
            if n % 2 == 0:
                return (x[int(n / 2 - 1)] + x[int(n / 2)]) / 2
            else:
                return x[int((n - 1) / 2)]
