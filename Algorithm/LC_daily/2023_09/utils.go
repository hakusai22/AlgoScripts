package _023_09

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/04 00:29
*/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
