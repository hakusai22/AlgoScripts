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

# -*- coding: utf-8 -*-
# @Author  : zero
# @Time    : 2022/11/28 21:51
if __name__ == '__main__':
    n = int(input())
    a = [str(i) for i in range(1, n + 1)]
    s = ""
    s = s.join(a)
    for i in permutations(s, n):
        print(" ".join(i))
