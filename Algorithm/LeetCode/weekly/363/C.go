package _63

import "sort"

/*
-*- coding: utf-8 -*-
@Author  : hakusai22
@Time    : 2023/09/18 22:42
*/
func maxNumberOfAlloys(n int, k int, budget int, composition [][]int,
	stock []int, cost []int) int {
	mx := int(1e9)
	ans := 0
	for _, com := range composition {
		res := sort.Search(mx, func(num int) bool {
			num++
			m := 0
			for i, s := range stock {
				if s < com[i]*num {
					m += (com[i]*num - s) * cost[i]
					if m > budget {
						return true
					}
				}
			}
			return false
		})
		ans = max(ans, res)
	}
	return ans
}

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
