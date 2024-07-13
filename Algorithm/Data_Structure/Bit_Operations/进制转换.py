# --idea
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2023/10/17 15:57

if __name__ == '__main__':
    decimal_num = 15

    # 转换为二进制
    binary_num = bin(decimal_num)
    print("二进制数：", binary_num)

    # 转换为二进制
    binary_num = bin(decimal_num)[2:]
    print("二进制数 除去前面两位：", binary_num)

    # 转换为八进制
    octal_num = oct(decimal_num)[2:]
    print("八进制数：", octal_num)

    # 转换为八进制
    octal_num = oct(decimal_num)
    print("八进制数 除去前面两位：", octal_num)

    # 转换为十六进制
    hexadecimal_num = hex(decimal_num)[2:]
    print("十六进制数：", hexadecimal_num)

    # 转换为十六进制
    hexadecimal_num = hex(decimal_num)
    print("十六进制数 除去前面两位：", hexadecimal_num)
