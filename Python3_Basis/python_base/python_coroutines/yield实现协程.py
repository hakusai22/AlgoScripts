# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/9/17 21:32

import time


# 协程之间执行任务按照一定顺序交替执行

def work1():
    while True:
        print("----work1---")
        yield
        time.sleep(0.5)


def work2():
    while True:
        print("----work2---")
        yield
        time.sleep(0.5)


def main():
    w1 = work1()
    w2 = work2()
    while True:
        next(w1)
        next(w2)


if __name__ == "__main__":
    main()
