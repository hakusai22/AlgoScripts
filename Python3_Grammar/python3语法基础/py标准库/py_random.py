# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/26 18:00
import random

if __name__ == '__main__':
    # 产生一个1到9之间的随机整数
    print(random.randint(1, 9))

    # 可以生成一个在0到1之间的随机数
    print(random.random())

    # 从一个序列中随机选择一个元素：
    a = [2, 3.2, "abc"]
    print(random.choice(a))

    b = list(range(20))
    print(b)

    # 函数random.shuffle()可以将序列中元素的顺序进行打乱
    print(random.shuffle(b))

    # 函数random.sample()可以从序列中不放回地随机采样元素，如采样3个元素：
    print(random.sample(b, 3))
