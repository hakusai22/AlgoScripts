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
# @Time    : 2024/07/13 17:43
# @题目     : https://leetcode.cn/problems/count-the-number-of-incremovable-subarrays-i/description/?envType=daily-question&envId=2024-07-10
# @参考     : https://leetcode.cn/problems/count-the-number-of-incremovable-subarrays-i/solutions/2577665/shuang-zhi-zhen-on-shi-jian-o1-kong-jian-3fl2/?envType=daily-question&envId=2024-07-10
# 时间复杂度 : 时间复杂度：O(n)，其中 n 为 nums 的长度。注意二重循环中的下标 i 和 j 都只会减小，不会变大。由于下标只会减小 O(n) 次，所以二重循环的总循环次数是 O(n) 的。


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1
        if i == n - 1:
            return n * (n + 1) // 2
        ans = i + 2

        j = n - 1
        while j == n - 1 or nums[j] < nums[j + 1]:
            while i >= 0 and nums[i] >= nums[j]:
                i -= 1
            ans += i + 2
            j -= 1
        return ans
