package _38

import "sort"

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/04/03 14:41
*/

func minOperations(a []int, qs []int) (ans []int64) {
	sort.Ints(a)
	sum := make([]int, len(a)+1)
	for i, v := range a {
		sum[i+1] = sum[i] + v
	}
	distanceSum := func(target int) int {
		i := sort.SearchInts(a, target)
		left := target*i - sum[i]
		right := sum[len(a)] - sum[i] - target*(len(a)-i)
		return left + right
	}
	for _, q := range qs {
		res := distanceSum(q)
		ans = append(ans, int64(res))
	}
	return
}
