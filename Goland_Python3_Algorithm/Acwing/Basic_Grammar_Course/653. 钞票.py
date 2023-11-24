# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/11/1 00:14

if __name__ == '__main__':
    a = [100, 50, 20, 10, 5, 2, 1]
    n = int(input())
    print(n)
    for i in a:
        print("%d nota(s) de R$ %d,00" % (n / i, i))
        n = n % i
