# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/11/2 22:34

if __name__ == '__main__':
    a, b, c = map(float, input().split())
    d, e, f = map(float, input().split())
    print("VALOR A PAGAR: R$ %.2lf" % (b * c + e * f))
