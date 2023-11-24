from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache
from typing import List, Optional
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
# @Author  : hakusai
# @Time    : 2023/09/04 00:43

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        def serialize_helper(node):
            if not node:
                return "None,"
            result = str(node.val) + ","
            left = serialize_helper(node.left)
            right = serialize_helper(node.right)
            result += left + right
            return result

        return serialize_helper(root)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        def deserialize_helper(values):
            value = values.pop(0)
            if value == "None":
                return None
            node = TreeNode(int(value))
            node.left = deserialize_helper(values)
            node.right = deserialize_helper(values)
            return node

        values = data.split(",")
        return deserialize_helper(values)
