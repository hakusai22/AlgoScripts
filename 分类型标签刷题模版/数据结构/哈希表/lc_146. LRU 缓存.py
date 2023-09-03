'''
Author: hakusai
Date: 2023-05-16 21:35:31
LastEditTime: 2023-05-16 21:58:04
Description: 
'''

from collections import Counter, defaultdict, deque
from functools import cache, lru_cache, reduce, cmp_to_key
from itertools import accumulate, combinations, permutations, product
from heapq import nsmallest, nlargest, heapify, heappop, heappush
from bisect import bisect_left, bisect_right
from math import factorial, gcd
from cmath import inf
from typing import List


class LRUCache:
    def __init__(self, capacity: int):
        self.data = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        s = self.data.get(key, -1)
        if s != -1:
            self.data.pop(key)
            self.data[key] = s
        return s

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data.pop(key)
        elif len(self.data) >= self.capacity:
            # iter() 函数用来生成迭代器
            # next()函数用来返回迭代器的下一个项目
            k = next(iter(self.data))
            self.data.pop(k)
        self.data[key] = value
