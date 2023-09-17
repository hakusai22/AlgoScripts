# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/9/22 00:06
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def find(start_idx, cur_path, remain_target):
            if remain_target == 0:
                ans.append(cur_path)
            else:
                for i in range(start_idx, len(candidates)):
                    if i > start_idx and candidates[i] == candidates[i - 1]:  # 不跳跃选取一样的元素
                        continue
                    if remain_target - candidates[i] < 0:  # 提前剪枝
                        break
                    find(i + 1, cur_path + [candidates[i]], remain_target - candidates[i])  # i+1因为不能选取重复元素

        ans = []
        candidates.sort()
        find(0, [], target)
        return ans


if __name__ == '__main__':
    res = Solution.combinationSum2(self=None, candidates=[1, 2, 3], target=5)
    print(res)
