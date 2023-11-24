# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/23 08:29
from collections import Counter
from string import digits


# 特判0是否为全部字符串
# 先用9-1每个字符去检查去查看在字符串中出现的次数，再用0去检查去查看在字符串中出现的次数，大于2次即可记录
# 将字符串反转，生成对称串
# 在剩余的字符串中找到除2后还有余数的最大数字
# 将两个字符串拼接形成最大回文数字


class Solution:
    def largestPalindromic(self, num: str) -> str:
        cnt = Counter(num)
        if cnt['0'] == len(num): return "0"  # 第一步

        s = ""
        # digits = '0123456789'
        for d in digits[:0:-1]:  # 第二步
            s += d * (cnt[d] // 2)
        if s:
            s += '0' * (cnt['0'] // 2)  # 第二步
        t = s[::-1]  # 第三步

        for d in digits[::-1]:  # 第四步
            if cnt[d] % 2:
                s += d
                break
        return s + t  # 第五步


if __name__ == '__main__':
    print(digits[:0:-1])
