# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/7/10 21:20

# 把 1 到 1000 的所有数字相加
from debugpy.common.compat import xrange

if __name__ == '__main__':
    numbers = list()

    for i in range(1000):
        numbers.append(i + 1)

    total = sum(numbers)
    print(total)


    def generate_numbers(n):
        num, numbers = 1, []
        while num < n:
            numbers.append(num)
        num += 1
        return numbers


    #total = sum(generate_numbers(1000))

    print(total)
    total = sum(range(1000 + 1))
    print(total)
    total = sum(xrange(1000 + 1))
    print(total)
