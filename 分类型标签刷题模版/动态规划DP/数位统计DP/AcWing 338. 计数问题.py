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
# @Time    : 2023/02/03 15:28

"""
    给定两个整数 a和 b，求 a和 b之间的所有数字中 0∼9的出现次数。
    例如，a=1024，b=1032，则 a和 b之间共有 9个数如下：
    1024 1025 1026 1027 1028 1029 1030 1031 1032
    其中 0 出现 10次，1 出现 10次，2 出现 7次，3 出现 3次等等…
    
    数据范围:
        0<a,b<100000000
"""
