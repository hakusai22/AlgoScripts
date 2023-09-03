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
    @functools.lru_cache(None) memory_search
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
    stack(列表) s.append(1) s.pop() /压栈/弹出栈顶元素
    
    列表推倒式 [i for i in range(100) if i % 3 == 0] 可切片,可索引,可重复
    字典推倒式 {key: len(key) for key in list}
    集合推倒式 {i ** 2 for i in (1, 2, 3) if i % 3 == 0}  不可索引,不可切片,不可重复元素
'''

# -*- coding: utf-8 -*-
# @Author  : wheat
# @Time    : 2023/01/13 16:02


"""
    题干给出 m(1≤m≤16)m(1≤m≤16) 个质数，我们可以通过容斥原理以及最小公倍数，
    将每个满足条件的数 num 只被统计一次（比如 num=6,P={2,3} 时，cnt=S2+S3−S2⋂S3）。
    由于元素之间的交集为质数之积（因为元素互质，积一定是最小公倍数），
    因此代码中 ⌊ntot⌋ 可以快速地得到 1→n1→n 中能整除 tot 的数。
"""
if __name__ == "__main__":
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    M = 1 << m

    res = 0
    # 枚举从1 到 1111...(m个1)的每一个集合状态, (至少选中一个集合)
    for i in range(1, 1 << m):
        t = 1  # 选中集合对应质数的乘积
        s = 0  # 选中的集合数量
        # 枚举当前状态的每一位
        for j in range(m):
            # 选中一个集合
            if i >> j & 1:
                s += 1
                # 乘积大于n, 则n/t = 0, 跳出这轮循环
                if t * p[j] > n:
                    t = -1
                    break
                t *= p[j]

        if t != -1:
            if s % 2:
                res += n // t # 奇数+ n//t为当前这种状态的集合数量
            else:
                res -= n // t # 偶数-

    print(res)
