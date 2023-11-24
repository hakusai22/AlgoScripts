# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/11/2 16:56
from collections import OrderedDict

if __name__ == '__main__':
    dict = OrderedDict({'a': 2})
    for key, value in dict.items():
        print(key, value)
