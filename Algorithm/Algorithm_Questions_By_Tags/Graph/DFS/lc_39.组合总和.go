package main

import "sort"

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/01/18 17:17
*/

// 主要在于递归中传递下一个数字
var (
	res  [][]int
	path []int
)

func combinationSum(candidates []int, target int) [][]int {
	res, path = make([][]int, 0), make([]int, 0, len(candidates))
	sort.Ints(candidates) // Sorting，为剪枝做准备
	dfs(candidates, 0, target)
	return res
}

func dfs(candidates []int, start int, target int) {
	if target == 0 { // target 不断减小，如果为0说明达到了目标值
		tmp := make([]int, len(path))
		copy(tmp, path)
		res = append(res, tmp)
		return
	}
	for i := start; i < len(candidates); i++ {
		if candidates[i] > target { // 剪枝，提前返回
			break
		}
		path = append(path, candidates[i])
		dfs(candidates, i, target-candidates[i])
		path = path[:len(path)-1]
	}
}
