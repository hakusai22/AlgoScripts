'''
Author: hakusai
Date: 2023-05-16 23:53:53
LastEditTime: 2023-05-16 23:53:59
Description: 
'''

lst = iter([0, 1, 2, 3])
print(lst)  # <list_iterator at 0x7fb83f6b9700>
for i in iter(lst):
    print(i)
    # 0
    # 1
    # 2
    # 3

#获得迭代器对象
lst = iter([0, 1, 2, 3])
while True:
    try:
        # 获得下一个值:
        print(next(lst))
        #0
        #1
        #2
        #3
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
