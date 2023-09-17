# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/8 22:01

def div(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Error: b should not be 0 !!")
    except Exception as e:
        print("Unexpected Error: {}".format(e))
    else:
        print('Run into else only when everything goes well')
    finally:
        print('Always run into finally block.')


if __name__ == '__main__':
    # tests
    div(2, 0)
    div(2, 'bad type')
    div(1, 2)

