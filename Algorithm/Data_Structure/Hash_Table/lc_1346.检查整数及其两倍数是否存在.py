# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/10/16 19:56
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        pre = set()
        for num in arr:
            if num % 2 == 0 and num // 2 in pre:
                return True
            if num * 2 in pre:
                return True
            pre.add(num)
        return False
