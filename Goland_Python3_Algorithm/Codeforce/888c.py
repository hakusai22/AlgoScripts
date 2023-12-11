
# --idea 
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2023/12/11 15:56
from collections import defaultdict

if __name__ == '__main__':
    s = input()
    idx = defaultdict(list)
    for i, x in enumerate(s):
        idx[x].append(i)
    ans = float('inf')
    for a in idx.values():
        a = [-1] + a + [len(s)]
        maxD = 0
        for i in range(1, len(a)):
            maxD = max(maxD, a[i] - a[i - 1])
        ans = min(ans, maxD)
    print(ans)

