
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/15 21:36


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        for length in range(n, 0, -1):
            for i in range(n-length+1):
                if s[i:i+length] == s[i:i+length][::-1]:
                    return s[i:i+length]

