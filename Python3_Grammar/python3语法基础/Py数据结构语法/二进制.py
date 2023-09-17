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
# @Time    : 2023/02/19 15:57

if __name__ == '__main__':
    num = 9
    print(bin(num))
    print(bin(num).count("1"))

    # lowbit
    print(num & -num)
    print(bin(num & -num))

    print(1<<1)
    print(1<<2)
    print(1<<3)
    print(1<<39)

    print(8>>1)
    print(1>>1)
    print(1>>2)

    """
    3.10 版中的新函数
    """
    print(num.bit_count())
