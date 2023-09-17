# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/10 23:03


# 在 Python 中用于生成随机数的模块是 random，在使用前需要 import. 如下例子可以酌情列举：
# random.random()：生成一个 0-1 之间的随机浮点数
# random.uniform(a, b)：生成[a,b]之间的浮点数
# random.randint(a, b)：生成[a,b]之间的整数
# random.randrange(a, b, step)：在指定的集合[a,b)中，以 step 为基数随机取一个数
# random.choice(sequence)：从特定序列中随机取一个元素，这里的序列可以是字符串，列表，元组等。
import random

if __name__ == '__main__':
    print(random.random())
    print(random.uniform(1, 3))
    print(random.randint(1, 100))
    print(random.randrange(1, 100, 2))
    print(random.choice([1, 2, 3, 4, 5, 6]))
    print(random.choice((1, 2, 3, 4, 5, 6)))
