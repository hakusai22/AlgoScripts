# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/26 16:50
import re

if __name__ == '__main__':
    # `re.match()`函数对字符串的开头进行匹配，返回第一个匹配对应的Match对象，否则返回None：
    pat = "\d+"
    s = "123abc123456"
    print(re.match(pat, s))
    print(re.match(pat, s).group(0))

    # 与re.match()函数不同，re.search()函数会用正则表达式去匹配字符串中所有的子串，如果找到，返回第一个匹配对应的Match对象，否则返回None：
    print(re.search(pat, s))  # <re.Match python_object; span=(3, 6), match='123'>
    print(re.search(pat, s).group(0))  # 123

    # re.split()使用指定的正则表达式作为分隔符，对字符串进行分割，其用法为
    pat = " +"
    s = "a b    c   d  e"
    print(re.split(pat, s))  # ['a', 'b', 'c', 'd', 'e']

    # re.sub()函数对字符串中正则表达式匹配的部分进行替换：
    replace = ";"
    print(re.sub(pat, replace, s))  # a;b;c;d;e

    # .	匹配除了换行符之外的内容
    # \w	匹配所有字母和数字字符
    # \d	匹配所有数字，相当于 [0-9]
    # \s	匹配空白，相当于 [\t\n\t\f\v]
    # \W,\D,\S	匹配对应小写字母形式的补
    # [...]	表示可以匹配的集合，支持范围表示如 a-z, 0-9 等
    # (...)	表示作为一个整体进行匹配
    # ¦	表示逻辑或
    # ^	表示匹配后面的子表达式的补
    # *	表示匹配前面的子表达式 0 次或更多次
    # +	表示匹配前面的子表达式 1 次或更多次
    # ?	表示匹配前面的子表达式 0 次或 1 次
    # {m}	表示匹配前面的子表达式 m 次
    # {m,}	表示匹配前面的子表达式至少 m 次
    # {m,n}	表示匹配前面的子表达式至少 m 次，至多 n 次
