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
# @Time    : 2023/02/01 13:34

"""

状态表示 ：f[i][j]
    集合：将a[1~i]变成b[1~j]的操作方式
    属性：min

     * 1. 删除操作 把a[i]删除后a[1~i]和b[1~j]匹配
     * 	那a[1~(i-1)]和b[1~j]匹配
     * 	f[i-1][j]+1
     * 2.插入操作
     * 	插入a[i]之后和b[j]匹配
     *   f[i][j-1]+1
     * 3.替换操作把a[i]改成b[j]之后想要a[1~i]与b[1~j]匹配
     * 	那么修改这一位之前，a[1~(i-1)]应该与b[1~(j-1)]匹配
     * 	若 a[i]!=b[j]
     *  f[i-1][j-1] + 1
     *      若a[i]==b[j]
     *  f[i-1]=f[j-1]
"""

if __name__ == '__main__':
    N = 1010
    f = [[0] * N for _ in range(N)]

    n = int(input())
    a = " " + input()
    m = int(input())
    b = " " + input()
    # 将 A 的前0个字母全部变成 B 的前m个字母，只能添加
    for i in range(1, m + 1):
        f[0][i] = i
    # 将 A 的前n个字母全部变成 B 的前0个字母，只能删除
    for i in range(1, n + 1):
        f[i][0] = i

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            f[i][j] = min(f[i - 1][j] + 1, f[i][j - 1] + 1)
            if a[i] == b[j]:
                f[i][j] = min(f[i][j], f[i - 1][j - 1])
            else:
                f[i][j] = min(f[i][j], f[i - 1][j - 1] + 1)

    print(f[n][m])
