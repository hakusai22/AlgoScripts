package main

import "fmt"

/*
 * @Author: hakusai
 * @Date: 2023-08-11 15:46:34
 * @LastEditTime: 2023-08-13 09:39:56
 * @Description: https://github.com/hakusai22
 */

func diagonalSum(mat [][]int) int {
	row := len(mat)
	col := len(mat[0])
	ans := 0
	for i := 0; i < row; i++ {
		ans += mat[i][i] + mat[row-1-i][i]
	}
	if row%2 == 1 {
		ans -= mat[row/2][col/2]
	}
	return ans
}

func main() {
	mat := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}
	result := diagonalSum(mat)
	fmt.Printf("result %v", result)
}
