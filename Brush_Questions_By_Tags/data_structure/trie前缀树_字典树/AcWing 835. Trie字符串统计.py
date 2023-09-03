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
# @Time    : 2022/11/21 16:06

if __name__ == '__main__':
    N = 100010
    # son[p][u] 表示p节点的孩子u是否存在于矩阵 son[][]存储子节点的位置，分支最多26条；
    son = [[0] * 26 for _ in range(N)]
    # cnt[]存储以某节点结尾的字符串个数
    cnt = [0] * N
    char = ['0'] * N
    # idx表示当前要插入的节点是第几个,每创建一个节点值+1
    idx = 0

    def insert(c):
        global idx
        p = 0
        for i in range(len(c)):
            # 将字母转化为数字
            u = ord(c[i]) - 97
            # 该节点不存在，创建节点,其值为下一个节点位置
            if not son[p][u]:
                idx += 1
                son[p][u] = idx
            # 使“p指针”指向下一个节点位置
            p = son[p][u]
        # //结束时的标记，也是记录以此节点结束的字符串个数
        cnt[p] += 1

    def query(c):
        global idx
        p = 0
        for i in range(len(c)):
            u = ord(c[i]) - 97
            # 该节点不存在，即该字符串不存在
            if not son[p][u]:
                return 0
            p = son[p][u]
        # 返回字符串出现的次数
        return cnt[p]

    n = int(input())
    while n:
        li = input().split()
        if li[0] == 'I':
            insert(li[1])
        else:
            print(query(li[1]))
        n -= 1
