# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/23 20:17

def removeDuplicates(s: str, k: int) -> str:
    n = len(s)
    stack = []
    for c in s:
        if not stack or stack[-1][0] != c:
            stack.append([c, 1])
        elif stack[-1][1] + 1 < k:
            stack[-1][1] += 1
        else:
            stack.pop()
    ans = ""
    for c, l in stack:
        ans += c * l
    return ans
