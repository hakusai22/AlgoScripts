
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/8 21:11

def main():
    try:
        with open('/Users/yinpeng/Desktop/wallhaven-l3vgor.jpeg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        with open('吉多.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError:
        print('指定的文件无法打开.')
    except IOError:
        print('读写文件时出现错误.')
    print('程序执行结束.')


if __name__ == '__main__':
    main()
