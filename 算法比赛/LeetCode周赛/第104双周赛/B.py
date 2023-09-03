'''
Author: hakusai
Date: 2023-05-14 01:30:39
LastEditTime: 2023-05-14 01:33:38
'''
from collections import Counter, defaultdict, deque
from functools import lru_cache, reduce, cmp_to_key
from itertools import accumulate, combinations, permutations, product
from heapq import nsmallest, nlargest, heapify, heappop, heappush
from bisect import bisect_left, bisect_right
from math import factorial, gcd
from cmath import inf
from typing import List


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for num in nums:
            num.sort(reverse=True)
        return sum(max(x) for x in zip(*nums))
