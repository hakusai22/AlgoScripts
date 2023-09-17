'''
Author: hakusai
Date: 2023-05-15 21:33:39
LastEditTime: 2023-05-15 21:36:16
'''


if __name__ == "__main__":
    aa=1
    print(id(aa))
    aa=2
    print(id(aa))

    a = []
    def fun(a):
        print(id(a))  # func_in 53629256
        a.append(1)
    print(id(a) )   # func_out 53629256
    fun(a)
    print(a)  # [1]
    # 在python中，strings, tuples, 和numbers是不可更改的对象，
    # 而 list, dict, set 等则是可以修改的对象