# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/9/21 23:33
import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))


if __name__ == '__main__':
    print(Solution.permute(self=None, nums=[1, 2, 3]))
    print(list(Solution.permute(self=None, nums=[1, 2, 3])))
