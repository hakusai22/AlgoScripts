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

if __name__ == '__main__':
    m, p = map(int, sys.stdin.readline().strip().split())

    # 线段树的节点
    class TreeNode(object):
        def __init__(self, l, r, v=0):
            self.l = l  # 该节点的左区间
            self.r = r  # 该节点的右区间
            self.v = v  # 线段树所要维护的属性，一般为区间最大、最小值或区间和等

    ### 线段树 ###

    # m为区间为[1,m]的长度，线段树的空间一般要为区间长度的四倍，可以加多一些余量
    tree = [None for i in range(4 * (m + 10))]

    # 对节点u进行建树，[l,r]对应的左子树和右子树为[l,mid]，[mid+1,r]
    def bulid(u, l, r):
        tree[u] = TreeNode(l, r)
        if l == r:
            return
        mid = l + r >> 1
        bulid(u << 1, l, mid)  # 递归建左子树
        bulid(u << 1 | 1, mid + 1, r)  # 递归建右子树

    # 根据子节点的信息，更新父节点u的信息
    # 这里需要根据线段树维护的属性来写，如维护最大值，则取所有子节点的最大值更新父节点的最大值
    def pushup(u):
        tree[u].v = max(tree[u << 1].v, tree[u << 1 | 1].v)

    # 将区间编号为a的点，值修改为x
    def modify(u, a, x):
        if tree[u].l == a and tree[u].r == a:
            tree[u].v = x
        else:
            mid = tree[u].l + tree[u].r >> 1
            if a <= mid:
                modify(u << 1, a, x)
            else:
                modify(u << 1 | 1, a, x)
            pushup(u)

    # 查询，查询[l,r]区间的属性，同样需要根据线段树维护的属性作修改
    def query(u, l, r):
        if tree[u].l >= l and tree[u].r <= r:
            return tree[u].v

        mid = tree[u].l + tree[u].r >> 1
        v = 0
        if l <= mid:
            v = query(u << 1, l, r)
        if r > mid:
            v = max(v, query(u << 1 | 1, l, r))
        return v

    # 题目处理
    bulid(1, 1, m)
    n, last = 0, 0
    for i in range(m):
        ope1, ope2 = sys.stdin.readline().strip().split()
        if ope1 == 'Q':
            L = int(ope2)
            last = query(1, n - L + 1, n)
            print(last)
        else:
            t = int(ope2)
            modify(1, n + 1, (t + last) % p)
            n += 1
