from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from typing import List, Tuple, Optional, Dict, Set
from collections import defaultdict, Counter, deque, OrderedDict, namedtuple
from sortedcontainers import SortedList, SortedDict, SortedSet
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache

'''
gcd(), ord(), chr(), lower(), upper() 最大公约数/ASCII字符数值/数值ASCII字符/小写/大写
startswith(s), endswith(s), find(), index(), count(s)  字符串是否以s开始的/字符串是否以s结尾的/查找返回的是索引/获取索引
isalpha(), isdigit(), space(),join()  判断是否全为字符/判断是否全为数字/判断是否为空格/拼接
eval() 字符串转换成列表、元组或者字典/
uniform(x, y), pow(x, y)# 随机生成下一个实数，它在[x,y]范围内/ x**y 运算后的值。
'''

'''
字典推倒式 {key: len(key) for key in list}
列表推倒式 [i for i in range(100) if i % 3 == 0] 可切片,可索引,可重复
集合推倒式 {i ** 2 for i in (1, 2, 3)}  不可索引,不可切片,不可重复元素
'''

'''
1.heapify(list):将序列list改变成heap结构
2.heappush(heap, item):向序列heap中插入一个item元素
3.heappop(heap):pop出heap堆中的最小值
4.heapreplace(heap, item):先pop出最小值，再向heap中添加item元素
5.heappushpop(heap, item): 与heapreplace方向相反
6.nlargest(n, iterable, key=None):返回heap的前n个最大的元素的list
7.nsmallest(n, iterable, key=None):返回heap的前n个最小的元素的list
'''


# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/11/6 14:04

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans, n = 0, len(costs)
        if candidates * 2 < n:
            pre = costs[:candidates]
            heapify(pre)
            suf = costs[-candidates:]
            heapify(suf)
            i, j = candidates, n - 1 - candidates
            while k and i <= j:
                if pre[0] <= suf[0]:
                    ans += heapreplace(pre, costs[i])
                    i += 1
                else:
                    ans += heapreplace(suf, costs[j])
                    j -= 1
                k -= 1
            costs = pre + suf
        costs.sort()
        return ans + sum(costs[:k])
