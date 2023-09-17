# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/7/10 19:45

if __name__ == '__main__':
    def filter_odd_numbers(num):
        if num % 2 == 0:
            return True
        else:
            return False


    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    filtered_numbers = filter(filter_odd_numbers, numbers)

    print(list(filtered_numbers))
