from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from typing import List, Tuple, Optional, Dict, Set
from collections import defaultdict, Counter, deque, OrderedDict, namedtuple
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, reduce
from copy import deepcopy
from io import BytesIO, IOBase
import random
import sys
import os

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

def I():
    return input()

def II():
    return int(input())

def IF():
    return float(input())

def MI():
    return map(int, input().split())

def MF():
    return map(float, input().split())

def LI():
    return list(input().split())

def LII():
    return list(map(int, input().split()))

def LFI():
    return list(map(float, input().split()))

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# -*- coding: utf-8 -*-
# @Author  : zero
# @Time    : 2022/11/21 11:29
"""
最小值和最大值分开来做，两个for循环完全类似，都做以下四步：
    1.解决队首已经出窗口的问题;
    2.解决队尾与当前元素a[i]不满足单调性的问题;
    3.将当前元素下标加入队尾;
    4.如果满足条件则输出结果;
"""

if __name__ == '__main__':
    n, k = MI()
    a = LII()
    N = 1000010
    q = [0 for i in range(N)]

    # 单调递增
    head = 0
    tail = -1
    for i in range(n):
        if head <= tail and i - k + 1 > q[head]:  # 判断队头是否已经滑出窗口
            head += 1
        #比较元素
        while head <= tail and a[q[tail]] >= a[i]:
            tail -= 1
        tail += 1
        q[tail] = i
        # 如果当前元素位置i大于k - 1位置，则输出
        if i - k + 1 >= 0:
            print(a[q[head]], end=' ')
    print()

    # 单调递减
    head = 0
    tail = -1
    for i in range(n):
        if head <= tail and i - k + 1 > q[head]:  # 判断队头是否已经滑出窗口
            head += 1
        while head <= tail and a[q[tail]] <= a[i]:
            tail -= 1
        tail += 1
        q[tail] = i
        if i - k + 1 >= 0:
            print(a[q[head]], end=' ')
