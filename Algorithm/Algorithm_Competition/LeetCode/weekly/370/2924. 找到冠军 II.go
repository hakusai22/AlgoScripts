package _70

/*
   --idea https://leetcode.cn/problems/find-champion-ii/description/
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/11/20 21:24
*/

func findChampion2(n int, edges [][]int) int {
	weak := make([]bool, n)
	for _, e := range edges {
		weak[e[1]] = true
	}
	ans := -1
	for i, w := range weak {
		if !w {
			if ans != -1 {
				return -1
			}
			ans = i
		}
	}
	return ans
}
