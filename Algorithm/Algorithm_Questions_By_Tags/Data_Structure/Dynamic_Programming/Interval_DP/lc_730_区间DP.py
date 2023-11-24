# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/10 09:36

# 类似普通区间dp，先枚举长度，再枚举左右端点
# 这里增加了一维，作为结尾字符，dp[k][i][j]表示在区间[i,j]中以第k个字符结尾的回文子序列的个数

def countPalindromicSubsequences(s: str) -> int:
    mod = 10 ** 9 + 7
    n = len(s)
    dp = [[[0] * n for _ in range(n)] for _ in range(4)]
    # 初始化长度为1的
    for i in range(n):
        dp[ord(s[i]) - 97][i][i] = 1
    # 区间dp
    for span in range(2, n + 1):
        for i in range(n - span + 1):
            j = i + span - 1
            for k in range(4):
                c = chr(k + 97)
                if s[i] != c:
                    dp[k][i][j] = dp[k][i + 1][j]
                elif s[j] != c:
                    dp[k][i][j] = dp[k][i][j - 1]
                elif s[i] == s[j] == c:
                    dp[k][i][j] = 2
                    if span >= 3:
                        for i0 in range(4):
                            dp[k][i][j] += dp[i0][i + 1][j - 1]
                            dp[k][i][j] %= mod
    return sum(dp[i][0][-1] for i in range(4)) % mod
