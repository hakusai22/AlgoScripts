package _023_09

/*
-*- coding: utf-8 -*-
@Author  : hakusai22
@Time    : 2023/09/13 08:46
*/
func checkValidGrid(grid [][]int) bool {
	if grid[0][0] != 0 {
		return false
	}

	n := len(grid)
	arr := make([][2]int, n*n)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			arr[grid[i][j]][0] = i
			arr[grid[i][j]][1] = j
		}
	}

	for i := 1; i < n*n; i++ {
		dx := abs(arr[i][0] - arr[i-1][0])
		dy := abs(arr[i][1] - arr[i-1][1])
		if dx*dy != 2 {
			return false
		}
	}
	return true
}
