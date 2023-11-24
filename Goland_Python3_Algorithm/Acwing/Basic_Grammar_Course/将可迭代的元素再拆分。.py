# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/11/2 17:01

from itertools import chain

if __name__ == '__main__':
    from_iterable = chain.from_iterable(['geeks', 'for', 'geeks'])
    print(list(from_iterable))
