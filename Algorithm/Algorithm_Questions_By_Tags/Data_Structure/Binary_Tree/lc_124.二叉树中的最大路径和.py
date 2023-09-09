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
# @Time    : 2022/12/09 15:37

"""
路径每到一个节点，有 3 种选择：1. 停在当前节点。2. 走到左子节点。3. 走到右子节点。
走到子节点，又面临这 3 种选择，递归适合处理这种规模不同的同一问题。

在当前子树中捞取的最大收益。分三种情况：
    1.路径停在当前子树的根节点，在当前子树的最大收益：root.val
    2.走入左子树，在当前子树的最大收益：root.val + dfs(root.left)
    3.走入右子树，在当前子树的最大收益：root.val + dfs(root.right)
    
    这对应了前面所说的三种选择，最大收益取三者最大：root.val+max(0, dfs(root.left), dfs(root.right))
    如果某个子树 dfs 结果为负，走入它，收益不增反减，该子树就没用，需杜绝走入，像对待 null 一样让它返回 0（壮士断腕）。
"""

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxsum = INFMIN

        def dfs(r):
            nonlocal maxsum  # 内部修改外部变量需要nonlocal，global
            if not r:
                return 0  # 遍历到null节点，收益0
            left = dfs(r.left)  # 左子树提供的最大路径和
            right = dfs(r.right)  # 右子树提供的最大路径和
            innerValue = left + right + r.val  # 当前子树内部的最大路径和
            maxsum = max(maxsum, innerValue)  # 挑战最大纪录
            outputMaxSum = max(left, right) + r.val  # 当前子树对外提供的最大和
            return max(0, outputMaxSum)  # 如果对外提供的路径和为负，直接返回0。否则正常返回

        dfs(root)
        return maxsum
