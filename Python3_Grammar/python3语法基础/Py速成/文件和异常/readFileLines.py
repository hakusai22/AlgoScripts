
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/8 20:55


import time


def main():
    # 一次性读取整个文件内容
    with open('/Users/yinpeng/Desktop/cbt_user_label.sql', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('/Users/yinpeng/Desktop/cbt_user_label.sql', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('/Users/yinpeng/Desktop/cbt_user_label.sql') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main()
