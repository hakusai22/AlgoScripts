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
# @Time    : 2023/01/31 15:29

if __name__ == '__main__':
    # 要把多重背包转化为0-1背包，N代表的是转化后的物品的种类数
    # 2000个物品可以用11个组合代表，然后总共有1000种物品，所以再冗余一下，就有了下面的N
    N = 11001
    # 正常的0-1背包的初始化
    v = [0] * N
    w = [0] * N
    f = [0] * N
    # 用cnt记录重新分组之后的个数
    cnt = 0
    # 下面是输入数据，然后进行打包，形成0-1背包
    n, m = map(int, input().split())

    while n:
        n -= 1
        a, b, s = map(int, input().split())
        # k代表当前几个该种类物品打包成一个种类
        k = 1
        while k <= s:
            cnt += 1
            v[cnt] = a * k
            w[cnt] = b * k
            s -= k
            k *= 2
        # 如果还有剩下的，那把剩下的这些全部作为一个种类打包起来，所以此时的个数是s个一包
        if s > 0:
            cnt += 1
            v[cnt] = a * s
            w[cnt] = b * s

    # 打包完成后，确认新的个数就是cnt
    n = cnt
    # 然后就和0-1背包一样了

    for i in range(1, n + 1):
        for j in range(m, v[i] - 1, -1):
            f[j] = max(f[j], f[j - v[i]] + w[i])

    print(f[m])
