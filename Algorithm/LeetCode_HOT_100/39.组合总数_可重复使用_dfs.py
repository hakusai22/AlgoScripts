# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/9/21 23:57
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        ans = []

        def find(s, use, remain):
            for i in range(s, len(candidates)):
                c = candidates[i]
                if c == remain:
                    ans.append(use + [c])
                if c < remain:
                    find(i, use + [c], remain - c)
                if c > remain:
                    return

        find(0, [], target)
        return ans


if __name__ == '__main__':
    print(Solution.combinationSum(self=None, candidates=[1, 2, 3], target=5))
