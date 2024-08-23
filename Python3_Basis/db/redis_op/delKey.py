from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache
from typing import List
import sys

sys.setrecursionlimit(10001000)

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')
INFMAX = float('inf')
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'

def alp(i):
    return chr(ord('a') + i % 26)  # i=0->'a', i=25->'z'

# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2024/03/21 15:15

if __name__ == '__main__':
    import redis

    def delete_redis_keys(start_num, end_num):
        # 连接到 Redis 服务器
        r = redis.Redis(host='xxxxx', port=6379, db=0)
        # 构建键名前缀
        key_prefix = "xxxx"
        # 删除指定范围内的键
        for i in range(start_num, end_num + 1):
            key = key_prefix + str(i) + "_DEBUG"
            # 使用 delete 方法删除键
            deleted = r.delete(key)
            if deleted:
                print(f"Deleted key: {key}")
            else:
                print(f"Key not found: {key}")

    # 调用函数删除指定范围内的键
    delete_redis_keys(51001, 51040)
