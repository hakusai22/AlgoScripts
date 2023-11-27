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

def rep():
    a = list(map(int, input().split()))
    return a

def sep():
    a = input().rstrip('\n')
    return a

# --idea  时间复杂度：O(nm)
#         空间复杂度：O(nm)
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2023/10/19 22:36
#
#
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        # dfs i j 在s中从0到i 和t中从0到j 最长的公共子串长度
        @cache
        def dfs(i, j):
            # 递归回去条件
            if i < 0 or j < 0:
                return 0
            # i和j位置的值一致
            if s[i] == t[j]:
                # 次数+1
                return dfs(i - 1, j - 1) + 1
            # 不相等的化 走i-1/j-1
            return max(dfs(i - 1, j), dfs(i, j - 1))

        return dfs(n - 1, m - 1)
