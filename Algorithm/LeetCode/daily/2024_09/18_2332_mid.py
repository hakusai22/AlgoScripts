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
# @Time    : 2024/09/19 22:41
# @题目     : https://leetcode.cn/problems/the-latest-time-to-catch-a-bus/description/?envType=daily-question&envId=2024-09-18
# @参考     : https://leetcode.cn/problems/the-latest-time-to-catch-a-bus/solutions/2920715/python3javacgotypescript-yi-ti-yi-jie-mo-dgzf/?envType=daily-question&envId=2024-09-18
# 时间复杂度 : O(n×logn+m×logm)


class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        global c
        buses.sort()
        passengers.sort()
        j = 0
        for t in buses:
            c = capacity
            while c and j < len(passengers) and passengers[j] <= t:
                c, j = c - 1, j + 1
        j -= 1
        # 若有空位，我们可以在公交车发车时 bus[∣bus∣−1] 到达公交站
        ans = buses[-1] if c else passengers[j]
        # 若无空位，我们可以找到上一个上车的乘客，顺着他往前找到没人到达的时刻。
        while j >= 0 and passengers[j] == ans:
            ans, j = ans - 1, j - 1
        return ans
