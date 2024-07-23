import time
from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby, pairwise
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, cache, reduce
from typing import List, Optional
import sys

import requests
import sched
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
# @Time    : 2024/07/23 00:02
# @题目     :
# @参考     :  
# 时间复杂度 :

if __name__ == '__main__':
    # 定义调用间隔（2分钟）
    # interval = 90
    # while True:
    #     response = requests.get("https://api-staging.bongmi.com/v1/cbt_meditation/category/603517991?debug_env_ignore_auth=true&app_flag=4096&language=2&platform_type=2&app_version=1.3.0&ab_param=a&localTimezone=Asia/Shanghai")
    #     print(response.status_code)
    #     time.sleep(interval)

    print(0x56259e50c000 - 0x56259d78e000)
    print(0x7fa1d064e000 - 0x7fa1d063d000)
    print(0x7fa1d084d000 - 0x7fa1d064e000)
    print(0x7fa1d084f000 - 0x7fa1d084d000)

    print(0x56259df52000-0x56259d78e000)


