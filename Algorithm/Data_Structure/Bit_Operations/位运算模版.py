# --idea
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2023/10/17 16:20

if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4, 5, 6, 7]
    # 交集
    print(set(arr1) & set(arr2))
    # 并集
    print(set(arr1) | set(arr2))
    # 差
    print(set(arr1) - set(arr2))
    # 差
    print(set(arr2) - set(arr1))

    for s in range(1 << 1):
        print(s)

    # 十进制转二进制函数： bin() 函数返回的字符串前缀为 "0b"，表示这是一个二进制数字。
    print(bin(400))
    # 十进制转八进制： oct() 函数返回的字符串前缀为 "0o"，表示这是一个八进制数字。
    print(oct(400))
    # 十进制转十六进制： hex() 函数返回的字符串前缀为 "0x"，表示这是一个十六进制数字。
    print(hex(400))
    # x进制转十进制 int(a,x)
    print(int("1111", 2))

    print(1<<2)
