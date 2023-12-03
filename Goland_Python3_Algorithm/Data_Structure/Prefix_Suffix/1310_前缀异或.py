# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/13 21:05
from python3语法基础.Py流式.py_itertools import accumulate
from operator import xor
from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prexor = list(accumulate([0] + arr, xor))
        return [prexor[i] ^ prexor[j + 1] for i, j in queries]
