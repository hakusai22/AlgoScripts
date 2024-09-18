import json
from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby, pairwise
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, cache, reduce
from typing import List, Optional
import sys
import os

from sortedcontainers import SortedList, SortedDict, SortedSet

sys.setrecursionlimit(10001000)

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')  # 负无穷
INFMAX = float('inf')  # 正无穷
PI = 3.141592653589793
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'

# @Author  : https://github.com/hakusai22
# @Time    : 2024/09/11 09:37
# @题目     :
# @参考     :  
# 时间复杂度 :

if __name__ == '__main__':
    domain_ff = os.getenv('DOMAIN_FF')
    for i in range(1, 91):
        re = []
        intro = domain_ff + "/wepray_business/reading_plan/bible_year/bible_in_a_year_content_intro_%d.mp3"
        verse = domain_ff + "/wepray_business/reading_plan/bible_year/content_verse_%d.mp3"
        end = domain_ff + "/wepray_business/reading_plan/bible_year/content_final_thoughts_%d.mp3"
        re.append(intro % i)
        re.append(verse % i)
        re.append(end % i)
        print(json.dumps(re))
