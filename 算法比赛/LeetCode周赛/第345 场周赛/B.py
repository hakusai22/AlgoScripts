'''
Author: hakusai
Date: 2023-05-14 12:03:53
LastEditTime: 2023-05-14 12:10:13
'''
from collections import Counter, defaultdict, deque
from functools import lru_cache, reduce, cmp_to_key
from itertools import accumulate, combinations, permutations, product
from heapq import nsmallest, nlargest, heapify, heappop, heappush
from bisect import bisect_left, bisect_right
from math import factorial, gcd
from cmath import inf
from operator import xor
from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return reduce(xor, derived) == 0


if __name__ == "__main__":
    print(Solution.doesValidArrayExist(self=None, derived=[1, 1, 0]))
    print(111)

