# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/10/16 06:40

class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        temp = sum(arr[:k])
        res = 1 if temp >= k * threshold else 0
        start = 0

        for i in range(k, len(arr)):
            temp = temp - arr[start] + arr[i]
            if temp >= threshold * k:
                res += 1
            start += 1

        return res
