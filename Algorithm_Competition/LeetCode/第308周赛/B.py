# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/9/1 23:54

# stack
class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for c in s:
            if c == '*':
                st.pop()
            else:
                st.append(c)
        return ''.join(st)


