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
# @Time    : 2022/12/04 01:27

"""
因此可以用线段树来求解，将线段树的节点的值定义为所管理区间的区间和，
这个区间和就表示此区间内有多少个时间单位被预定过了

空间复杂度就是O(N)
线段树的一次操作的时间复杂度为O(logN)（即树高的常数倍复杂度）
"""

class Node:
    def __init__(self, left=None, right=None, val=0, lazy=0):
        """
        left:   左孩子
        right:  右孩子
        val:    值
        lazy:   懒惰标记，是0说明没有懒惰标记，是正数说明这里的懒惰标记还未下放
        """
        self.left = left
        self.right = right
        self.val = val
        self.lazy = lazy

class SegmentTree:
    def __init__(self, size):
        """
        size:   线段树的总大小（根节点管理的区间的长度）
        """
        self.size = size
        self.root = Node()
        return

    def pushDown(self, node, start, end):
        """
        向下更新，并传递懒惰更新标志
        node:   当前节点
        s:      start，当前节点管理的左边界（含）
        e:      end，当前节点管理的右边界（含）
        """
        mid = start + end >> 1
        if node.left is None:
            node.left = Node()
        if node.right is None:
            node.right = Node()
        if node.lazy == 0:
            return
        node.left.val += node.lazy * (mid - start + 1)
        node.right.val += node.lazy * (end - mid)
        node.left.lazy += node.lazy
        node.right.lazy += node.lazy
        node.lazy = 0
        return

    def pushUp(self, node):
        """
        向上更新，要求node的两个子节点均已更新完
        node:   当前节点
        """
        node.val = node.left.val + node.right.val
        return

    def update(self, node, start, end, left, right, add):
        """
        更新闭区间[l, r]，给此区间内的每个值，都加上add
        闭区间[l, r]和当前区间[start, end]的交集一定非空
        node:   当前节点
        start，当前节点管理的左边界（含）
        end，当前节点管理的右边界（含）
        left，要更改的区间的左边界
        right，要更改的区间的右边界
        add:    addition，增量
        """
        if left <= start and end <= right:
            node.val += add * (end - start + 1)
            node.lazy += add
            return

        self.pushDown(node, start, end)
        mid = start + end >> 1

        if left <= mid:
            self.update(node.left, start, mid, left, right, add)
        if right > mid:
            self.update(node.right, mid + 1, end, left, right, add)

        self.pushUp(node)
        return

    def query(self, node, start, end, left, right):
        """
        查询闭区间[l, r]的值
        闭区间[l, r]和当前区间[s, e]一定是有交集的
        node:   当前节点
        s:      start，当前节点管理的左边界（含）
        e:      end，当前节点管理的右边界（含）
        l:      left，要更改的区间的左边界
        r:      right，要更改的区间的右边界
        """

        # [start,end] 在[left,right]之间 直接返回该线段对应的数量
        if left <= start and end <= right:
            return node.val

        self.pushDown(node, start, end)
        mid = start + end >> 1

        ans = 0
        # 左节点查询 [start,mid] 搜索 [left,right]线段
        if left <= mid:
            ans += self.query(node.left, start, mid, left, right)
        # 右节点查询 [mid+1,end] 搜索 [left,right]
        if right > mid:
            ans += self.query(node.right, mid + 1, end, left, right)
        return ans

class MyCalendar:

    def __init__(self):
        self.size = 10 ** 9
        self.seg_tree = SegmentTree(size=self.size)

    def book(self, start: int, end: int) -> bool:
        # 判断区间[start,end] 存在的size是不是>0
        if self.seg_tree.query(self.seg_tree.root, 0, self.size, start, end - 1) > 0:
            return False
        # 更新【start,end】区间size的数量
        self.seg_tree.update(self.seg_tree.root, 0, self.size, start, end - 1, 1)
        return True
