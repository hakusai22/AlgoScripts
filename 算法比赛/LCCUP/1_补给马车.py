'''
Author: hakusai
Date: 2023-04-22 17:33:12
LastEditTime: 2023-04-22 21:26:45
'''
import random, sys, os, math, gc
from collections import Counter, defaultdict, deque
from functools import lru_cache, reduce, cmp_to_key
from itertools import accumulate, combinations, permutations, product
from heapq import nsmallest, nlargest, heapify, heappop, heappush
from io import BytesIO, IOBase
from copy import deepcopy
from bisect import bisect_left, bisect_right
from math import factorial, gcd
from operator import mul, xor
from types import GeneratorType
from cmath import inf
from typing import List

class Solution:
    def supplyWagon(self, a: List[int]) -> List[int]:
        n = len(a)
        for _ in range((n + 1) // 2):
            mx = inf
            k = -1
            for i in range(len(a) - 1):
                if a[i] + a[i + 1] < mx:
                    mx = a[i] + a[i + 1]
                    k = i
            a = a[:k] + [a[k] + a[k + 1]] + a[k + 2:]
        return a


if __name__ == '__main__':
    s = Solution()
    print(s.supplyWagon([1, 2, 3, 4, 5]))
