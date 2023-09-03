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

MOD = int(1e9 + 7)
INF = int(1e20)
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
# @Time    : 2022/12/04 17:25
"""
一个未排序数组，要找出数字连续最长序列，且时间复杂度为n，因此只能进行一次遍历且不能进行排序，考虑使用并查集
"""

class UnionFind:
    """
    self.parent = {100: 100, 4: 4, 200: 200, 1: 1, 3: 3, 2: 2}，自己的根节点就是自己。
    self.count是一个字典，形如 根节点:元素个数，表示根节点后面连接子节点的个数。
    如 1:3 表示1为根节点，后面还连着两个连续的元素，即1→2→3，共3个元素。
    """
    def __init__(self, nums):
        self.parent = {num: num for num in nums}
        self.cnt = defaultdict(lambda: 1)

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        if y not in self.parent:
            return 1
        # 寻找x, y的根节点，记为root1, root2
        root1, root2 = self.find(x), self.find(y)

        # 如果root1 == root2，直接返回self.cnt[root1]或者self.cnt[root2]
        # 表示当前的数与之前已经出现的一些数字能构成连续序列
        if root1 == root2:
            return self.cnt[root1]

        # 将root2的根节点改为root1，如下面步骤5中的图所示，将两棵子树合并
        self.parent[root2] = root1
        # 两棵子树合并时，现在的树的元素个数就是这两棵树之和
        self.cnt[root1] += self.cnt[root2]
        return self.cnt[root1]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        union = UnionFind(nums)
        res = 1
        for num in nums:
            res = max(res, union.union(num, num + 1))
        return res
