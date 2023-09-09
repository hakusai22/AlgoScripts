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
# @Time    : 2023/01/31 09:43

"""
    有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。
    第 i 件物品的体积是 vi ，价值是 wi。
    求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
    输出最大价值。
    
    /*
     * 状态f[j]定义：N件物品，背包容量j下的最优解。
     * (1) 如果不装第 i 件物品，那么问题就转化为“前 i−1 件物品放入容量为 j的背包中的最大价值”
       (2) 如果装第 i件物品，那么问题就转化为“前 i−1 件物品放入剩下的容量为 j−v[i] 的背包中的最大价值”
       状态转移方程为：f[j] = max(f[j], f[j - v[i]] + w[i] 
     */
"""

if __name__ == '__main__':
    N = 1010
    v = [0] * N
    w = [0] * N
    f = [0] * N

    n, m = map(int, input().split())
    for i in range(1, n + 1):
        v[i], w[i] = map(int, input().split())

    for i in range(1, n + 1):
        # 和01背包问题的遍历体积j时从逆序开始 保证前面的体积更新不会受到影响
        # 逆序是为了保证更新当前状态时，用到的状态是上一轮的状态，保证每个物品只有一次或零次;
        # 只有当枚举的背包容量 >= v[i] 时才会更新状态
        for j in range(m, v[i] - 1, -1):
            f[j] = max(f[j], f[j - v[i]] + w[i])
    print(f[m])
