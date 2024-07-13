# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/25 17:50

# 1.括号与括号之间为一段
# 2.遇到左括号，当前这一段存入stack
# 3.遇到右括号，当前这一段翻转，可以与前一段拼接了。
# 4.一直进行。即可得到结果。

class Solution:
    def reverseParentheses(s: str) -> str:
        stk = []
        word = ""
        for c in s:
            if c == '(':  # 遇到新的一段了
                stk.append(word)  # 这段进stk
                word = ""  # 新的一段开始统计
            elif c == ')':
                word = stk.pop(-1) + word[::-1]  # 这一段要翻转了，与前面的一段可以接起来
            else:
                word += c  # 统计入当前的这一段
        return word


if __name__ == '__main__':
    print(Solution.reverseParentheses("(u(love)i)"))
