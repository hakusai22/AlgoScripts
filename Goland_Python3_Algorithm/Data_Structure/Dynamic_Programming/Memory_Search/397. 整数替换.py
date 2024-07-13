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



def rep():
    a = list(map(int, input().split()))
    return a

def sep():
    a = input().rstrip('\n')
    return a

# --idea 
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2023/11/27 14:47
#
# 给定一个正整数 n ，你可以做如下操作：
# 如果 n 是偶数，则用 n / 2替换 n 。
# 如果 n 是奇数，则可以用 n + 1或n - 1替换 n 。
# 返回 n 变为 1 所需的 最小替换次数 。
class Solution:
    def integerReplacement(self, n: int) -> int:
        # dfs n 需要最少的操作数量
        @cache
        def dfs(n):
            if n == 1:
                return 0
            if n % 2 == 0:
                ans = dfs(n // 2) + 1
            else:
                ans = min(dfs(n + 1), dfs(n - 1)) + 1

            return ans

        return dfs(n)
