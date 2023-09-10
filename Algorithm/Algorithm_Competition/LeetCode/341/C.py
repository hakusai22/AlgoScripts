from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache
import sys

sys.setrecursionlimit(10001000)

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')
INFMAX = float('inf')
PI = 3.141592653589793
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'

def alp(i):
    return chr(ord('a') + i % 26)  # i=0->'a', i=25->'z'

def input():
    return sys.stdin.readline().rstrip()

def end(r=-1):
    print(r)
    exit()

# -*- coding: utf-8 -*-
# @Author  : wink
# @Time    : 2023/04/16 10:09

class Solution:
    def addMinimum(self, word: str) -> int:
        stack = []
        count = 0
        for c in word:
            if c == "a":
                stack.append(c)
            elif c == "b":
                if not stack or stack[-1] == "b":
                    stack.extend(["a", "c"])
                    count += 2
                else:
                    stack.pop()
                    stack.append(c)
                    stack.append("c")
                    count += 1
            else:
                if not stack or stack[-1] == "b":
                    stack.extend(["a", "b"])
                    count += 2
                else:
                    stack.pop()
                    stack.pop()
                    count += 1
        if len(stack) == 1:
            count += 2
        elif len(stack) == 2:
            count += 1
        return count
