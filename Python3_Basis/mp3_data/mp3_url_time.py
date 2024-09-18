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
# @Time    : 2024/09/13 18:14
# @题目     :
# @参考     :  
# 时间复杂度 :

import requests
from mutagen.mp3 import MP3
from io import BytesIO

def get_mp3_time(url):
    response = requests.get(url)
    response.raise_for_status()
    audio = MP3(BytesIO(response.content))
    duration_sec = audio.info.length
    return int(duration_sec)

if __name__ == '__main__':
    with open("./testament.txt", 'r', encoding='utf-8') as file:
        index = 1
        for line in file:
            res = []
            for url in json.loads(line):
                res.append(get_mp3_time(url))
            print(json.dumps(res))
