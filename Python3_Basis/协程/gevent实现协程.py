# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/9/17 22:56

import gevent


def work(n):
    for i in range(n):
        # 获取当前协程
        print(gevent.getcurrent(), i)


if __name__ == '__main__':
    g1 = gevent.spawn(work, 5)
    g2 = gevent.spawn(work, 5)
    g3 = gevent.spawn(work, 5)
    g1.join()
    g2.join()
    g3.join()
