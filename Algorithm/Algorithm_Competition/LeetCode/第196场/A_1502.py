# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/23 21:39

# https://leetcode.cn/problems/can-make-arithmetic-progression-from-sequence/
from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        return len(set(arr[i] - arr[i + 1] for i in range(len(arr) - 1))) == 1


if __name__ == '__main__':
    arr = [3, 5, 1]
    arr.sort()
    print(set(arr[i] - arr[i + 1] for i in range(len(arr) - 1)))
