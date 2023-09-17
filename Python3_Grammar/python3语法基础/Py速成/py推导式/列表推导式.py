# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/10/10 09:30

if __name__ == '__main__':
    names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
    name_news = [name.upper() for name in names if len(name) > 3]
    print(name_news)

    multiples = [i for i in range(100) if i % 3 == 0]
    print(multiples)
