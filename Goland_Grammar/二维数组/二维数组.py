'''
Author: hakusai
Date: 2023-05-19 16:13:02
LastEditTime: 2023-05-19 16:13:04
Description: 
'''
"""
@Author: hakusai 
@Date: 2023-05-17 23:15:27 
@LastEditTime: 2023-05-19 16:09:14 
@Description: 
"""

def case_1():
    # 一：先创建再赋值，为赋值的为默认值0
    tdArray_1 = [[0 for _ in range(3)] for _ in range(3)]
    tdArray_1[0][0] = 0
    tdArray_1[0][1] = 1
    tdArray_1[0][2] = 2
    tdArray_1[1][0] = 3
    tdArray_1[2][1] = 4
    # 二：创建并赋值
    tdArray_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"tdArray_1：{tdArray_1}   数据类型：{type(tdArray_1)}")
    print(f"tdArray_2：{tdArray_2}   数据类型：{type(tdArray_2)}")

def case_2():
    # 二维数组双for循环嵌套遍历
    tdArray = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for i in range(len(tdArray)):
        for j in range(len(tdArray[i])):
            print(tdArray[i][j])

def case_3():
    # 二维数组for range遍历
    tdArray = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for indexOne, valueOne in enumerate(tdArray):
        print(f"arrayOne: {indexOne} {valueOne}")
        for indexTwo, valueTwo in enumerate(tdArray[indexOne]):
            print(f"arrayTwo: {indexTwo} {valueTwo}")

    for i, v1 in enumerate(tdArray):
        print("i: ", i, " v1: ", v1)
        for j, v2 in enumerate(tdArray[i]):
            print("j: ", j, " v2: ", v2)
            

if __name__ == '__main__':
    case_1()
    case_2()
    case_3()
