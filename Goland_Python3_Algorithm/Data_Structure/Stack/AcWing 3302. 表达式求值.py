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
# @Time    : 2022/11/21 16:50

if __name__ == '__main__':
    dic = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    op = []
    num = []

    def new_eval():
        b = num.pop()
        a = num.pop()
        c = op.pop()
        x = 0
        if c == '+':
            x = a + b
        elif c == '-':
            x = a - b
        elif c == '*':
            x = a * b
        else:
            x = int(a / b)
        num.append(x)

    a = I()
    n = len(a)
    i = 0
    while i < n:
        c = a[i]
        if c.isdigit(): # 如果是数字则直接存入
            x = 0
            j = i
            while j < n and a[j].isdigit():
                x = x * 10 + int(a[j])
                j += 1
            i = j - 1
            num.append(x)
        elif c == '(':
            op.append(c)
        elif c == ')': # 出现右括号就可以计算与最近的左括号之间的操作
            while op[-1] != '(':
                new_eval()
            op.pop() # 删除已经计算的左括号
        else:  # 运算符
            while len(op) and dic[op[-1]] >= dic[c]:
                new_eval()
            op.append(c)
        i += 1   # 后移，指向下一个字符

    while len(op): # 计算剩下的操作
        new_eval()
    print(num[-1])
