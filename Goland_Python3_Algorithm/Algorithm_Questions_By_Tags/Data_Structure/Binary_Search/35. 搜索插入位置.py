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

# 数值和字母进行转换 ord()函数是把字符转换成ASCII码 chr()函数是把ASCII码转换成字符
def alp(i):
    return chr(ord('a') + i % 26)  # i=0->'a', i=25->'z'

# lcm 最小公倍数 gcd 最大公约数
def lcm(x, y):
    return x * y // gcd(x, y)

# 快速幂
def qpow(x, y):
    ans = 1
    while y:
        if y & 1:
            ans *= x
        x *= x
        y >>= 1
    return ans

# 求组合数
def Comb(n, m, p):
    a = (factorial(n)) % p
    b = (qpow(factorial(m), (p - 2), p)) % p
    c = (qpow(factorial(n - m), (p - 2), p)) % p
    return a * b * c % p

# lucas求组合数
def Lucas(n, m, p):
    if m == 0:
        return 1
    return Comb(n % p, m % p, p) * Lucas(n // p, m // p, p) % p

def rep():
    a = list(map(int, input().split()))
    return a

def sep():
    a = input().rstrip('\n')
    return a

# --idea 模板1就是在满足check()的区间内找到左边界
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2023/10/18 23:25

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # bisect_left函数返回排序数组中值等于k的最左索引，如果没有，就返回插入后其索引
        # return bisect_left(nums,target)
        if target > nums[len(nums) - 1]: return len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + r >> 1
            if target == nums[mid]: return mid
            if target < nums[mid]:
                r = mid
            else:
                l = mid + 1
        return l
