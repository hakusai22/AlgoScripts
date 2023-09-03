from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from typing import List, Tuple, Optional, Dict, Set
from collections import defaultdict, Counter, deque, OrderedDict, namedtuple
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, reduce

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')
INFMAX = float('inf')
'''
    @functools.lru_cache(None) 记忆化搜索
    字符串切片 str[::-1] # 字符串翻转  str[0:1]  左闭右开
    列表 l.append(1) l.extend([1,2,3]) l.insert(1,3) l.remove(1),(del list[0]) ,l.pop() ,l.pop(0), l.sort(reverse=True) ,l.reverse() 列表操作 
    ASCII ord('a'), chr(98), /ASCII字符数值/数值ASCII字符
    字符串 s.lower(), s.upper() ,s.title() /小写/大写/首字母大写
    字符串 str.replace('k','8',2) ,str.strip() ,str.rstrip(), str.lstrip(),  #将字符串里的k替换为8,前两个/删除空白
    字符串 str.startswith(s), str.endswith(s), str.find(s), str.index(s), str.count(s)  字符串是否以s开始的/字符串是否以s结尾的/查找s返回的是索引/获取s的索引
    字符串 s.isalpha(), s.isdigit(), s.isspace(), "_".join([1,2])  判断是否全为字符/判断是否全为数字/判断是否为空格/使用_拼接列表
    字典 m.keys(), m.values(), m.items() 字段key的列表/value的列表/ key,value值对
    eval("1,2,3") 字符串转换成列表、元组或者字典/
    公式 gcd(a,b), lcm(a,b), pow(a,b), sqrt(x), ceil(x), floor(x) /最大公约数/最小公倍数/ x的y次方/ x的平方根 /向上/向下
    堆 heapfiy([]),heappush(1), heappop(),nlargest(3,list),nsmallest(3,list),heapreplace(list,4) list转为最小堆/添加元素/弹出最小值并返回/返回堆最大的3个元素/返回堆中最小的3个元素/弹出堆顶元素,压入4
    双端队列 d.append(1), appendleft(1), d.pop(), d.popleft(), d.clear(),d.count(1), d.reverse() /队尾添加/队头添加
    栈(列表) s.append(1) s.pop() /压栈/弹出栈顶元素
    
    列表推倒式 [i for i in range(100) if i % 3 == 0] 可切片,可索引,可重复
    字典推倒式 {key: len(key) for key in list}
    集合推倒式 {i ** 2 for i in (1, 2, 3) if i % 3 == 0}  不可索引,不可切片,不可重复元素
'''

# -*- coding: utf-8 -*-
# @Author  : wheat
# @Time    : 2023/01/15 11:36


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        N = 510
        b = [[0] * N for _ in range(N)]
        c = [[0] * n for _ in range(n)]

        def insert1(x1, y1, x2, y2, c):
            b[x1][y1] += c
            b[x2 + 1][y1] -= c
            b[x1][y2 + 1] -= c
            b[x2 + 1][y2 + 1] += c

        for x1, y1, x2, y2 in queries:
            insert1(x1, y1, x2, y2, 1)

        # 通过对差分矩阵求前缀和
        for i in range(0, n):
            for j in range(0, n):
                b[i][j] += b[i - 1][j] + b[i][j - 1] - b[i - 1][j - 1]
                c[i][j] = b[i][j]
        return c
