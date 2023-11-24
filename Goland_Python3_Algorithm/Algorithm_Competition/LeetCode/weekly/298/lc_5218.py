# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/19 12:19
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        # 9 [9,99]
        for i in range(1, 11):
            kk = k * i
            if kk <= num and kk % 10 == num % 10:
                return i
        return -1
