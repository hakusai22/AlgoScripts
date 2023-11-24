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
# @Time    : 2023/02/01 17:30

"""
    给定两个字符串 A 和 B ，现在要将 A 经过若干操作变为 B，可进行的操作有：
        1. 删除–将字符串 A 中的某个字符删除。
        2. 插入–在字符串 A 的某个位置插入某个字符。
        3. 替换–将字符串 A 中的某个字符替换为另一个字符。
    现在请你求出，将 A 变为 B 至少需要进行多少次操作。
    
    1)删除操作：把a[i]删掉之后a[1~i]和b[1~j]匹配
            所以之前要先做到a[1~(i-1)]和b[1~j]匹配
                f[i-1][j] + 1
    2)插入操作：插入之后a[i]与b[j]完全匹配，所以插入的就是b[j] 
            那填之前a[1~i]和b[1~(j-1)]匹配
                f[i][j-1] + 1 
    3)替换操作：把a[i]改成b[j]之后想要a[1~i]与b[1~j]匹配 
            那么修改这一位之前，a[1~(i-1)]应该与b[1~(j-1)]匹配
                f[i-1][j-1] + 1
            但是如果本来a[i]与b[j]这一位上就相等，那么不用改，即
                f[i-1][j-1] + 0
    那么f[i][j]就由以上三个可能状态转移过来，取个min

"""

if __name__ == '__main__':
    N = 15
    M = 1010
    f = [[0] * N for _ in range(N)]
    a = [[0] * N for _ in range(M)]

    def distance(a, b):
        la = len(a) - 1
        lb = len(b) - 1

        for i in range(1, lb + 1):
            f[0][i] = i
        for i in range(1, la + 1):
            f[i][0] = i

        for i in range(1, la + 1):
            for j in range(1, lb + 1):
                f[i][j] = min(f[i - 1][j] + 1, f[i][j - 1] + 1)
                if a[i] == b[j]:
                    f[i][j] = min(f[i][j], f[i - 1][j - 1])
                else:
                    f[i][j] = min(f[i][j], f[i - 1][j - 1] + 1)
        return f[la][lb]

    n, m = map(int, input().split())
    for i in range(n):
        a[i] = " " + input()

    while m:
        m -= 1
        li = input().split()
        b = " " + li[0]
        lmt = int(li[1])
        res = 0
        for i in range(n):
            if distance(a[i], b) <= lmt:
                res += 1
        print(res)
