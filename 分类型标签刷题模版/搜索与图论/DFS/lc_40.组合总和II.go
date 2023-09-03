package main

import "sort"

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/01/18 17:23
*/

// **使用used数组**
var (
	res2  [][]int
	path2 []int
	used  []bool
)

func combinationSum2(candidates []int, target int) [][]int {
	res2, path2 = make([][]int, 0), make([]int, 0, len(candidates))
	used = make([]bool, len(candidates))
	sort.Ints(candidates) // 排序，为剪枝做准备
	dfs2(candidates, 0, target)
	return res2
}

func dfs2(candidates []int, start int, target int) {
	if target == 0 { // target 不断减小，如果为0说明达到了目标值
		tmp := make([]int, len(path2))
		copy(tmp, path2)
		res2 = append(res2, tmp)
		return
	}
	for i := start; i < len(candidates); i++ {
		if candidates[i] > target { // 剪枝，提前返回
			break
		}
		// used[i - 1] == true，说明同一树枝candidates[i - 1]使用过
		// used[i - 1] == false，说明同一树层candidates[i - 1]使用过
		if i > 0 && candidates[i] == candidates[i-1] && used[i-1] == false {
			continue
		}
		path2 = append(path2, candidates[i])
		used[i] = true
		dfs2(candidates, i+1, target-candidates[i])
		used[i] = false
		path2 = path2[:len(path2)-1]
	}
}
