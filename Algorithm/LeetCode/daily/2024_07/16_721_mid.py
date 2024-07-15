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
# @Time    : 2024/07/15 10:39
# @题目     : https://leetcode.cn/problems/accounts-merge/description/?envType=daily-question&envId=2024-07-15
# @参考     :   https://leetcode.cn/problems/accounts-merge/solutions/2844186/ha-xi-biao-dfspythonjavacgojsrust-by-end-z9nh/?envType=daily-question&envId=2024-07-15
# 时间复杂度 : 时间复杂度：O(LlogL)，其中 L 是 accounts 中所有字符串的长度之和。瓶颈在排序上。


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emial_to_idx = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                emial_to_idx[email].append(i)

        def dfs(index):
            vis[index] = True
            for email in accounts[index][1:]:
                if email in email_set:
                    continue
                email_set.add(email)
                for j in emial_to_idx[email]:
                    if not vis[j]:
                        dfs(j)

        ans = []
        vis = [False] * len(accounts)
        for i, b in enumerate(vis):
            if not b:
                email_set = set()
                dfs(i)
                ans.append([accounts[i][0]] + sorted(email_set))
        return ans
