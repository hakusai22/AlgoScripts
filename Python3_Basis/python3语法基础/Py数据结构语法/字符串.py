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
# @Time    : 2023/02/19 16:23

if __name__ == '__main__':
    str = " qwertyuiop "
    print(str.count("q"))

    print(str.capitalize())
    print(str.strip())
    print(str.find("q", 1, 10))

    print(str.isspace())
    print(str.index("t", 1, 10))
    print(str.isdigit())
    print(" ".join(str))
    print(str.split("t"))
    print(str.isalpha())
    print(str.upper())
    print(str.lower())

    print(str.replace("q","z"))
