from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache
import sys
from typing import List

sys.setrecursionlimit(10001000)

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')
INFMAX = float('inf')
PI = 3.141592653589793
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'

def alp(i):
    return chr(ord('a') + i % 26)  # i=0->'a', i=25->'z'

def input():
    return sys.stdin.readline().rstrip()

def end(r=-1):
    print(r)
    exit()

# -*- coding: utf-8 -*-
# @Author  : wink
# @Time    : 2023/04/15 22:28

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        # 获取行数和列数
        m, n = len(grid), len(grid[0])
        # 初始化结果数组
        ans = [0] * n
        # 遍历每一列
        for j in range(n):
            # 初始化最大宽度为0
            max_width = 0
            # 遍历当前列的每个数字，计算该列的最大宽度
            for i in range(m):
                max_width = max(max_width, len(str(grid[i][j])))
            # 更新结果数组
            ans[j] = max_width
        # 返回结果数组
        return ans
