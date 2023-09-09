'''
Author: hakusai
Date: 2023-05-17 01:00:19
LastEditTime: 2023-05-17 01:12:50
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


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union_Find
        pa = list(range(n))

        def find(x):
            if x != pa[x]:
                pa[x] = find(pa[x])
            return pa[x]

        def union(i, j):
            x, y = map(find, [i, j])
            if x == y:
                return
            pa[x] = y
        deg = [0]*n  # 节点的度
        for a, b in edges:
            union(a, b)
            deg[a] += 1
            deg[b] += 1

        # 如果连通分量有n 个点，那么只有每个点都与剩余 n−1 个点相连，即度为 n−1 时，这个连通分量是完全连通分量。
        group = defaultdict(list)
        for x in range(n):
            group[find(x)].append(x)
        ans = 0
        for g in group.values():
            l = len(g)
            if all(deg[x] == l-1 for x in g):  # 检查节点的度是不是都符合要求
                ans += 1
        return ans


if __name__ == "__main__":
    print(Solution.countCompleteComponents(
        self=None, n=6, edges=[[0, 1], [0, 2], [1, 2], [3, 4]]))
