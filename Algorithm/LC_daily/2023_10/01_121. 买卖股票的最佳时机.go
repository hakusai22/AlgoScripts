package _023_10

/*
	枚举 + 维护前缀最小值
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/10/06 15:24
*/

func maxProfit(prices []int) int {
	var ans int
	mi := prices[0]
	for _, v := range prices {
		ans = max(ans, v-mi)
		mi = min(mi, v)
	}
	return ans
}
