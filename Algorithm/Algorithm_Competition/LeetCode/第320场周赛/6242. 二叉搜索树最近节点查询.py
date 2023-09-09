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

class Solution:
    def closestNodes(self, root: Optional[TreeNode], q: List[int]) -> List[List[int]]:
        a = []

        def dfs(rt):
            if rt is None:
                return
            dfs(rt.left)
            a.append(rt.val)
            dfs(rt.right)

        dfs(root)
        # print(a)
        ans = []
        for x in q:
            # bisect_left()函数返回排序数组中值等于k的最左索引，如果没有，就返回插入后其索引 (在所有已存在值的左侧)
            # bisect_right()函数返回排序数组中值等于k的最右索引 + 1，如果没有，就返回插入后其索引 (在所有已存在值的右侧)
            # bisect()函数返回排序数组中值等于k的最右索引 + 1，如果没有，就返回插入后其索引 (在所有已存在值的右侧)
            l = bisect_right(a, x)
            r = bisect_left(a, x)
            val = [-1, -1]
            if l > 0:
                val[0] = a[l - 1]
            if r < len(a):
                val[1] = a[r]
            ans.append(val)
        return ans


