# --idea
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2023/12/11 15:02

class D:
    pass

class C(D):
    pass

class B(C):
    def show(self):
        print("i am B")
    pass

class G:
    pass

class F(G):
    pass

class E(F):
    def show(self):
        print("i am E")
    pass

class A(B, E):
    pass

if __name__ == '__main__':
    a = A()
    a.show()
