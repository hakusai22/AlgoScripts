package _023_09

import "sort"

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/19 08:36
*/

func minCapability(nums []int, k int) int {
	return sort.Search(1e9, func(mx int) bool {
		pre, cur := 0, 0
		for _, x := range nums {
			if x > mx {
				pre = cur
			} else {
				pre, cur = cur, max(cur, pre+1)
			}
		}
		return cur >= k
	})
}
