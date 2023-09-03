'''
Author: hakusai
Date: 2022-12-04 12:15:19
LastEditTime: 2023-05-16 22:49:34
Description: 
'''
# 封装为类的模版
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def merge(self, a, b):
        self.parent[self.find(b)] = self.find(a)


# 原生模版
N = 100010
p = [0] * N

# find函数，用于返回x的祖宗节点
# 同时压缩往回搜寻节点的路径


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]
