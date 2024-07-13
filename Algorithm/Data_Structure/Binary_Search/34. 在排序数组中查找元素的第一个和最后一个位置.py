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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/11/22 21:22
#
# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        # 模板1就是在满足check()的区间内找到左边界
        if len(arr) == 0:
            return [-1, -1]
        # 搜索出左端点的下标
        # 区间[l, r]被划分成 [l, mid] 和 [mid+1, r]时使用
        # mid归于左边, r = mid, mid选择 不 +1
        # l, r = 0, len(arr) - 1
        # while l < r:
        #     mid = (l + r) // 2
        #     if arr[mid] >= target:
        #         r = mid
        #     else:
        #         l = mid + 1
        # if arr[l] != target:
        #     return [-1, -1]
        # left = l

        # 模板2在满足check()的区间内找到右边界
        # 搜索出右端点的下标
        # 区间[l, r]被划分成 [l, mid-1] 和 [mid, r]时使用
        # mid归于右边, l = mid, mid选择 +1
        # l, r = 0, len(arr) - 1
        # while l < r:
        #     mid = (l + r + 1) >> 1
        #     if arr[mid] <= target:
        #         l = mid
        #     else:
        #         r = mid - 1
        # return [left, l]

        # bisect_left函数返回排序数组中值等于k的最左索引，如果没有，就返回插入后其索引
        # bis_right函数返回排序数组中值等于k的最右索引+1，如果没有，就返回插入后其索引
        i = bisect_left(arr, target)
        if not (i < len(arr) and arr[i] == target):
            return [-1, -1]

        return [i, bisect_right(arr, target) - 1]
