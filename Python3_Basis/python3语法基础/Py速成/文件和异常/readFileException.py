
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/8 20:54
def main():
    f = None
    try:
        f = open('/Users/yinpeng/Desktop/cbt_user_label.sql', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


if __name__ == '__main__':
    main()