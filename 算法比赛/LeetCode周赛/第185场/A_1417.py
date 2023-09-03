# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/23 20:48


# https://leetcode.cn/problems/reformat-the-string/

# 字符个数比数字的个数多1时，需要满足 a1a
# 字符个数比数字的个数少1时，需要满足 1a1
# 字符个数比数字的个数相等时，需要满足 a1 或者 1a
import re


class Solution:
    def reformat(self, s: str) -> str:
        alph_str = ''.join(alph for alph in re.split(r'[0-9]', s) if alph)
        num_str = ''.join(num for num in re.split(r'[a-z]', s) if num)

        if abs(len(alph_str) - len(num_str)) > 1:
            return ''

        res = ''.join(alph + num for alph, num in zip(alph_str, num_str))
        if len(alph_str) - len(num_str) == 0:
            return res
        return res + alph_str[-1] if len(alph_str) > len(num_str) else num_str[-1] + res


if __name__ == '__main__':
    # for if 连用
    x = [1, 2, 3, 4, 5]
    c = [k for k in x if k % 2 == 1]
    print(c)  # [1, 3, 5]

    x = [1, 2, 3, 4, 5]
    y = [5, 6, 7, 8, 9]

    c = [a + b for a in x for b in y if a % 2 == 1 and b % 2 == 1]
    print(c)  # [6, 8, 10, 8, 10, 12, 10, 12, 14]

    s = "qweqrwewe12312asrqwe12312"
    print(''.join(alph for alph in re.split(r'[0-9]', s) if alph))
    print(''.join(num for num in re.split(r'[a-z]', s) if num))
    print(list(zip(''.join(alph for alph in re.split(r'[0-9]', s) if alph),
              ''.join(num for num in re.split(r'[a-z]', s) if num))))
