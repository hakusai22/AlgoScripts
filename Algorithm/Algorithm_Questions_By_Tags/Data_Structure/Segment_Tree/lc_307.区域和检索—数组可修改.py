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
# @Time    : 2022/12/03 23:52
"""
给你一个数组 nums ，请你完成两类查询。
其中一类查询要求 更新 数组  nums 下标对应的值
另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right
实现 NumArray 类：
NumArray(int[] nums) 用整数数组 nums 初始化对象
void update(int index, int val) 将 nums[index] 的值 更新 为 val
int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 （即，nums[left] + nums[left + 1], ..., nums[right]）
 
示例 1：
输入：
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
输出：
[null, 9, null, 8]

解释：
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // 返回 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1,2,5]
numArray.sumRange(0, 2); // 返回 1 + 2 + 5 = 8
"""
'''BIT：Binary Indexed Tree Fenwick_Tree'''
"""
复杂度分析
记 n=len(nums)n=len(nums)，则
时间复杂度：
    - 构建树状数组：O(n)
    - 更新树状数组：O(logn)
    - 区域和检索：O(logn)
空间复杂度：
    - 构建树状数组：O(n)
    - 更新树状数组：O(1)
    - 区域和检索：O(1)
"""
'''ST：Segment Tree Segment_Tree'''

class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.n = n
        self.tree = [0] * n + nums  # 线段树ST长度为2n
        for i in range(n - 1, 0, -1):  # [1, n-1] 倒序添加，子节点之和
            # ST[2i]和ST[2i+1]分别为ST[i]的左右子节点
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index: int, val: int) -> None:
        i = index + self.n  # nums下标转换到ST下标
        delta = val - self.tree[i]  # 变更值
        while i:  # 自下而上进行更新
            self.tree[i] += delta
            i //= 2

    def sumRange(self, left: int, right: int) -> int:
        i, j = left + self.n, right + self.n  # nums下标转换到ST下标
        summ = 0
        while i <= j:
            if i % 2 == 1:  # ST[i]是右子节点
                summ += self.tree[i]  # 计入ST[i]，并i+1（转向下一个区间）
                i += 1
            if j % 2 == 0:  # ST[j]是左子节点
                summ += self.tree[j]  # 计入ST[j]，并j-1（转向上一个区间）
                j -= 1
            i, j = i // 2, j // 2
        return summ
