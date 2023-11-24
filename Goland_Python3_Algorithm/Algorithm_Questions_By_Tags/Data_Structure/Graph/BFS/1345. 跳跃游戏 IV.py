# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/10/16 19:41
from collections import defaultdict, deque
from typing import List


class Solution:
    def minJumps(arr: List[int]) -> int:
        n = len(arr)
        d = defaultdict(list)
        for i, x in enumerate(arr):
            d[x].append(i)

        q = deque([[0, 0]])
        vis = {0, }
        while q:
            i, step = q.popleft()
            if i == n - 1: return step
            v = d[arr[i]]
            v.append(i + 1)
            if i: v.append(i - 1)
            while v:
                j = v.pop()
                if j in vis: continue
                q.append([j, step + 1])
                vis.add(j)
            # d.pop(arr[i])

        # return -1


if __name__ == '__main__':
    arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
    Solution.minJumps(arr)
