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
# @Time    : 2023/02/03 15:46

"""
    求把 N×M 的棋盘分割成若干个 1×2 的长方形，有多少种方案。
    例如当 N=2，M=4 时，共有 5种方案。当 N=2，M=3 时，共有 3种方案。
    
    1. 所谓的状态压缩DP，就是用二进制数保存状态。为什么不直接用数组记录呢？因为用一个二进制数记录方便作位运算
    2. 本题等价于找到所有横放 1 X 2 小方格的方案数，因为所有横放确定了，那么竖放方案是唯一的。
    3. 用f[i][j]记录第i列第j个状态。j状态位等于1表示上一列有横放格子，本列有格子捅出来。转移方程很简单，本列的每一个状态都由上列所有“合法”状态转移过来f[i][j] += f[i - 1][k]
    4. 两个转移条件： i 列和 i - 1列同一行不同时捅出来 ； 本列捅出来的状态j和上列捅出来的状态k求或，得到上列是否为奇数空行状态，奇数空行不转移。
    5. 初始化条件f[0][0] = 1，第0列只能是状态0，无任何格子捅出来。返回f[m][0]。第m + 1列不能有东西捅出来。
"""

if __name__ == '__main__':
    N = 12
    M = 1 << N
    st = [False] * M
    while 1:
        n, m = map(int, input().split())
        f = [[0] * M for _ in range(N)]
        if n == 0 and m == 0:
            break

        for i in range(1 << n):
            st[i] = True
            cnt = 0
            for j in range(n):
                if i >> j & 1:
                    if cnt & 1:
                        st[i] = False
                        cnt = 0
                else:
                    cnt += 1
            if cnt & 1:
                st[i] = False

        f[0][0] = 1
        for i in range(1, m + 1):
            for j in range(1 << n):
                for k in range(1 << n):
                    if j & k == 0 and st[j | k]:
                        f[i][j] += f[i - 1][k]

        print(f[m][0])
