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

'''
heaqp
deque
permutations(arr,r) 返回的是一个长度为 r 的所有可能排列，无重复元素
combinations(arr,r) 返回的是一个长度为r的组合，它是有序的，无重复元素
bisect()和bisect_right()等同 函数返回排序数组中值等于k的最左索引，如果没有，就返回插入后其索引
bis_right函数返回排序数组中值等于k的最右索引+1，如果没有，就返回插入后其索引
gcd(), ord(), chr(), lower(), upper() 最大公约数/ASCII字符数值/数值ASCII字符/小写/大写
startswith(s), endswith(s), find(), index(), count(s)  字符串是否以s开始的/字符串是否以s结尾的/查找返回的是索引/获取索引
isalpha(), isdigit(), space(),join()  判断是否全为字符/判断是否全为数字/判断是否为空格/拼接
eval() 字符串转换成列表、元组或者字典/
uniform(x, y), pow(x, y)# 随机生成下一个实数，它在[x,y]范围内/ x**y 运算后的值。
字典推倒式 {key: len(key) for key in list}
列表推倒式 [i for i in range(100) if i % 3 == 0] 可切片,可索引,可重复
集合推倒式 {i ** 2 for i in (1, 2, 3)}  不可索引,不可切片,不可重复元素
'''

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

# --idea 
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2023/12/01 16:50
#
# 给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数，citations 已经按照 升序排列 。计算并返回该研究者的 h 指数。
# h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （n 篇论文中）至少 有 h 篇论文分别被引用了至少 h 次。
# 请你设计并实现对数时间复杂度的算法解决此问题。

# 如果有至少 x 篇论文的引用次数大于等于 x，那么对于任意 y<x，其引用次数也一定大于等于 y。这存在着单调性。
# 二分枚举 h，获取满足条件的最大 h。由于要满足 h 篇论文至少被引用 h 次

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 左开右闭区间写法 [l,r) 模版二 找右边界
        l, r = 0, len(citations)
        while l < r:
            mid = (l + r + 1) >> 1
            # 引用次数最多的 mid 篇论文，引用次数均 >= mid
            if citations[-mid] >= mid:
                l = mid  # 询问范围缩小到 (mid, right]
            else:
                r = mid - 1  # 询问范围缩小到 (left, mid-1]
        return l
