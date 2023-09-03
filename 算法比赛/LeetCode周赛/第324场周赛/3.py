from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e, lcm
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from typing import List, Tuple, Optional, Dict, Set
from collections import defaultdict, Counter, deque, OrderedDict, namedtuple
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby, pairwise
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, reduce
from copy import deepcopy
from io import BytesIO, IOBase
import random
import sys
import os

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')
INFMAX = float('inf')
'''
gcd(), ord(), chr(), lower(), upper() 最大公约数/ASCII字符数值/数值ASCII字符/小写/大写
startswith(s), endswith(s), find(), index(), count(s)  字符串是否以s开始的/字符串是否以s结尾的/查找返回的是索引/获取索引
isalpha(), isdigit(), space(),join()  判断是否全为字符/判断是否全为数字/判断是否为空格/拼接
eval() 字符串转换成列表、元组或者字典/
uniform(x, y), pow(x, y)# 随机生成下一个实数，它在[x,y]范围内/ x**y 运算后的值。
字典推倒式 {key: len(key) for key in list}
列表推倒式 [i for i in range(100) if i % 3 == 0] 可切片,可索引,可重复
集合推倒式 {i ** 2 for i in (1, 2, 3)}  不可索引,不可切片,不可重复元素
gcd为最大公约数, lcm为最小公倍数。
'''

def I():
    return input()

def II():
    return int(input())

def FI():
    return float(input())

def MII():
    return map(int, input().split())

def MFI():
    return map(float, input().split())

def LI():
    return list(input().split())

def LMII():
    return list(map(int, input().split()))

def LMFI():
    return list(map(float, input().split()))

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# -*- coding: utf-8 -*-
# @Author  : zero
# @Time    : 2022/12/18 12:46

"""
把度数为奇数的节点记到 odd 中，记 mm 为odd 的长度，分类讨论：

如果 m=0，那么已经符合要求。
如果 m=2，记x=odd[0],y=odd[1]：
    如果 x 和 y 之间没有边，那么连边之后就符合要求了。
    如果 x 和 y 之间有边，那么枚举 [1,n] 的所有不为 x 和 y 的点 i，由于 i 的度数一定是偶数，
    如果 i 和 x 以及 i 和 y 之间没有边，那么连边之后就符合要求了。
如果 m=4，记 a=odd[0],b=odd[1],c=odd[2],d=odd[3]：
    如果 a 和 b 以及 c 和 d 之间没有边，那么连边之后就符合要求了。
    如果 a 和 c 以及 b 和 d 之间没有边，那么连边之后就符合要求了。
    如果 a 和 d 以及 b 和 c 之间没有边，那么连边之后就符合要求了。

"""

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        s, deg = set(), Counter()
        for x, y in edges:
            s.add((x, y))
            s.add((y, x))
            deg[x] += 1
            deg[y] += 1
        odd = [i for i, d in deg.items() if d % 2]
        m = len(odd)
        if m == 0:
            return True
        if m == 2:
            x, y = odd
            return (x, y) not in s or any(
                i != x and i != y and (i, x) not in s and (i, y) not in s
                for i in range(1, n + 1)
            )
        if m == 4:
            a, b, c, d = odd
            return (a, b) not in s and (c, d) not in s or \
                   (a, c) not in s and (b, d) not in s or \
                   (a, d) not in s and (b, c) not in s
        return False
