package C

import (
	redblacktree "github.com/emirpasic/gods/trees/redblacktree"
	"math"
)

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/08/13 12:54
*/

func minAbsoluteDifference(nums []int, x int) int {
	tree := redblacktree.NewWithIntComparator()
	ans := math.MaxInt
	n := len(nums)
	for i := x; i < n; i++ {
		tree.Put(nums[i-x], nums[i-x])
		if v, e := tree.Ceiling(nums[i]); e {
			ans = min(ans, abs(nums[i]-v.Value.(int)))
		}
		if v, e := tree.Floor(nums[i]); e {
			ans = min(ans, abs(nums[i]-v.Value.(int)))
		}
	}
	return ans
}
func abs(a int) int {
	if a > 0 {
		return a
	}
	return -a
}
func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}
