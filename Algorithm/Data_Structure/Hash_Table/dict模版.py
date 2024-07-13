from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque, OrderedDict
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby, pairwise
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, cache, reduce
from typing import List, Optional
import sys

from sortedcontainers import SortedList, SortedDict, SortedSet

sys.setrecursionlimit(10001000)

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')  # 负无穷
INFMAX = float('inf')  # 正无穷
PI = 3.141592653589793
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'

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



def rep():
    a = list(map(int, input().split()))
    return a

def sep():
    a = input().rstrip('\n')
    return a

# --idea 
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2023/10/20 16:00

if __name__ == '__main__':
    # python 根据 key，value 排序字典
    d = {'d': 4, 'a': 1, 'b': 2, 'c': 3}
    # dict sort by **key** and reverse
    dict(sorted(d.items()))  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    dict(sorted(d.items(), reverse=True))  # {'d': 4, 'c': 3, 'b': 2, 'a': 1}

    # dict sort by **value** and reverse
    dict(sorted(d.items(), key=lambda kv: kv[1]))  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    dict(sorted(d.items(), key=lambda kv: kv[1], reverse=True))  # {'d': 4, 'c': 3, 'b': 2, 'a': 1}

    # 获取字典对应的最大值对应的 key,value
    mydict = {'A': 4, 'B': 10, 'C': 0, 'D': 87}
    maximum = max(mydict, key=mydict.get)  # Just use 'min' instead of 'max' for minimum.
    maxk, maxv = maximum, mydict[maximum]
    # 或者
    maxk, maxv = max(mydict.items(), key=lambda k: k[1])

    # 支持默认值的有序字典 (OrderedDict and defaultdict)  (注意是 key 插入顺序不是字典序)
    # https://stackoverflow.com/questions/6190331/how-to-implement-an-ordered-default-dict
    od = OrderedDict()  # collections.OrderedDict()
    i = 0
    od[i] = od.get(i, 0) + 1  # 间接实现了 defaultdict(int) ，同时保持了插入字典的 key 顺序
