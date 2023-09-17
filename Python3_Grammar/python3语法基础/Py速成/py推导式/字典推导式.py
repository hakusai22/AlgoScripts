# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/10/10 09:33


if __name__ == '__main__':
    listdemo = ['Google', 'Runoob', 'Taobao']
    newdict = {key: len(key) for key in listdemo}
    print(newdict)

    dic = {x: x ** 2 for x in (2, 4, 6)}
    print(dic)
