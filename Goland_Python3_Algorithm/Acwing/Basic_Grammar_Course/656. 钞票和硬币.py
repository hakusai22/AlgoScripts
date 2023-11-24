# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/11/2 23:17

if __name__ == '__main__':
    m = eval(input())

    n = m * 100

    p = (10000, 5000, 2000, 1000, 500, 200)
    c = (100, 50, 25, 10, 5, 1)

    print("NOTAS:")
    for i in range(0, len(p)):
        print(int(n / p[i]), "nota(s) de R$ " + f'{p[i] / 100:.2f}')
        n = n % p[i]

    print("MOEDAS:")
    for i in range(0, len(c)):
        print(int(n / c[i]), "moeda(s) de R$ " + f'{c[i] / 100:.2f}')
        n = n % c[i]
