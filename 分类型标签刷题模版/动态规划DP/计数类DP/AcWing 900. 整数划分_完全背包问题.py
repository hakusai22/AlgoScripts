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
# @Time    : 2023/02/02 15:00

"""
    一个正整数 n 可以表示成若干个正整数之和，形如：n=n1+n2+…+nk ，其中 n1≥n2≥…≥nk,k≥1。
    我们将这样的一种表示称为正整数 n 的一种划分。
    现在给定一个正整数 n，请你求出 n 共有多少种不同的划分方法。
    
    把1,2,3, … n分别看做n个物体的体积，这n个物体均无使用次数限制，问恰好能装满总体积为n的背包的总方案数（完全背包问题变形）
    完全背包问题，f[i][j]表示从1~i中选总体积为j的所有方案的数量
    f[j] = f[j] + f[j-i];
"""
if __name__ == '__main__':
    N = 1010
    mod = 1e9 + 7
    f = [0] * N

    # // 一个都不选的情况下 而且体积 为0 所以 数量只有一个;
    f[0] = 1

    n = int(input())
    # 比如f[1] , 表示一个都不选 但是体积为 1 的时候 所以一定为 0;
    for i in range(1, n + 1):
        # 完全背包用不到i - 1 层 从小到大枚举体积就OK
        for j in range(i, n + 1):
            f[j] = int((f[j] + f[j - i]) % mod)
    print(f[n])
