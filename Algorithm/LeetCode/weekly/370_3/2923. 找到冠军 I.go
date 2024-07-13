package _70_3

/*
--idea
-*- coding: utf-8 -*-
@Author  : hakusai22
@Time    : 2023/11/20 21:24
*/
func findChampion(grid [][]int) int {
next:
	for j := range grid[0] {
		for _, row := range grid {
			if row[j] > 0 { // 有队伍可以击败 j
				continue next
			}
		}
		return j
	}
	panic(-1)
}
