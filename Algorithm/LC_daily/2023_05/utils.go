package _023_05

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/03 15:45
*/

func min(a, b int) int {
	if b < a {
		return b
	}
	return a
}
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}
