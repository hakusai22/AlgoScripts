# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/8 22:32

from typing import List


def __init__(matrix: List[List[int]]):
    if not matrix or not matrix[0]:
        M, N = 0, 0
    else:
        M, N = len(matrix), len(matrix[0])
    preSum = [[0] * (N + 1) for _ in range(M + 1)]
    for i in range(M):
        for j in range(N):
            preSum[i + 1][j + 1] = preSum[i][j + 1] + preSum[i + 1][j] - preSum[i][j] + matrix[i][j]


def sumRegion(row1: int, col1: int, row2: int, col2: int) -> int:
    return preSum[row2 + 1][col2 + 1] - preSum[row2 + 1][col1] - preSum[row1][col2 + 1] + \
           preSum[row1][col1]


if __name__ == '__main__':
    list = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    print(__init__(list))
