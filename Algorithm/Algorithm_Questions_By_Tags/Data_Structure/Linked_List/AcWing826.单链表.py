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
# @Time    : 2022/12/24 11:20

if __name__ == '__main__':
    N = 100010
    head = -1
    e = [0] * N
    ne = [0] * N
    idx = 0

    # 头结点插入操作
    def insert_head(x):
        global idx, head
        e[idx] = x
        ne[idx] = head
        head = idx
        idx += 1

    # 插入到第k个点的后面
    def insert(k, x):
        global idx
        e[idx] = x
        ne[idx] = ne[k]
        ne[k] = idx
        idx += 1

    # 删除第k个点的后面结点
    def remove(k):
        ne[k] = ne[ne[k]]

    n = II()
    while n:
        li = input().split()
        if li[0] == 'H':
            x = int(li[1])
            insert_head(x)
        elif li[0] == 'I':
            k, x = int(li[1]), int(li[2])
            insert(k - 1, x)
        else:
            if li[1] == '0':
                head = ne[head]
            k = int(li[1])
            remove(k - 1)
        n -= 1

    i = head
    res = []
    while i != -1:
        res.append(e[i])
        i = ne[i]
    print(" ".join(map(str, res)))
