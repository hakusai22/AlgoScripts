# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/11/2 22:42

if __name__ == '__main__':
    a, b, c = map(float, input().split())
    print("TRIANGULO: %.3lf" % (a * c / 2))
    print("CIRCULO: %.3lf" % (3.14159 * c * c))
    print("TRAPEZIO: %.3lf" % ((a + b) * c / 2))
    print("QUADRADO: %.3lf" % (b * b))
    print("RETANGULO: %.3lf" % (a * b))
