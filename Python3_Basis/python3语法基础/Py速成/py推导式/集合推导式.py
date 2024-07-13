# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/10/10 09:35
if __name__ == '__main__':
    setnew = {i ** 2 for i in (1, 2, 3)}
    print(setnew)

    a = {x for x in 'asdasdascadasdasewrteydfgdf   d' if x not in 'a'}
    print(a)