from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from typing import List, Tuple, Optional, Dict, Set
from collections import defaultdict, Counter, deque, OrderedDict, namedtuple
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, reduce

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')
INFMAX = float('inf')

# -*- coding: utf-8 -*-
# @Author  : wheat
# @Time    : 2023/02/15 17:58

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        ans = nums[0]
        for num in nums[1:]:
            # math库里有直接计算最大公约数的函数
            ans = gcd(num, ans)
            # 如果截至目前计算得到的最大公约数已经为1，那么可以提前退出
            if ans == 1:
                return True
        return ans == 1
