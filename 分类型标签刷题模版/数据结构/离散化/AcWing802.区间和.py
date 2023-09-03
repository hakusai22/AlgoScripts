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
# @Time    : 2022/12/24 10:46

"""
离散化可以理解为压缩化
* 压缩前和压缩后需要有一个对应关系，之间的桥梁便是二分法
"""

if __name__ == '__main__':
    N = 300010  # 最多要用到三十万个坐标：插入(x),查询(l,r)

    n, m = MII()
    a = [0] * N  # 离散索引：离散前的坐标所拥有值
    S = [0] * (N + 1)  # 前缀和数组
    alls = []  # 所有使用过的坐标
    add = []  # 二元组，(插入值,插入坐标)
    query = []  # 二元组，(l,r)

    def find(x):
        # 给定离散前的值，找出离散后的值
        # 整数二分，找出>=x的第一个数即可
        l = 0
        r = len(alls) - 1
        while l < r:
            mid = (l + r) // 2
            if alls[mid] >= x:
                r = mid
            else:
                l = mid + 1
        return l + 1

    # 收集插入操作
    for i in range(n):
        x, c = MII()
        add.append((x, c))
        alls.append(x)

    # 收集询问操作
    for i in range(m):
        l, r = MII()
        query.append((l, r))
        alls.append(l)
        alls.append(r)

    alls = list(set(sorted(alls)))  # 对alls进行去重（因为原坐标是具有唯一性的）

    # 对离散后的数组进行插入操作
    for x, c in add:
        x2 = find(x)  # 离散数组中的位置
        a[x2 - 1] += c  # 保持对应关系，返回的索引

    # 对离散数组求前缀和
    for i in range(1, N + 1):
        S[i] = S[i - 1] + a[i - 1]

    # 进行m次询问
    for l, r in query:
        xl = find(l)
        xr = find(r)
        print(S[xr] - S[xl - 1])
