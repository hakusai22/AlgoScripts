# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/19 12:31
from collections import deque


class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # 子序列， k最多32位
        ans = 0
        cnt = 0
        length = 0
        q = deque()
        for r, v in enumerate(s):
            cnt <<= 1
            if v == '1':
                cnt += 1
                q.append(r)
            while cnt > k:
                v = 1 << (r - q.popleft())
                cnt -= v
                length -= 1
            length += 1
            ans = max(ans, length)
        return ans
