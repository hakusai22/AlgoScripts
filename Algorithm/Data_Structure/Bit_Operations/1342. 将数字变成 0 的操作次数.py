# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/10/16 06:35
class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        x = num
        while x != 0:
            if x & 1:
                x -= 1
            else:
                x >>= 1
            step += 1

        return step
