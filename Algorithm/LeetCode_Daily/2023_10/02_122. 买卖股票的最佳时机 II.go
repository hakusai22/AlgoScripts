package _023_10

/*
   --idea 贪心
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/10/06 15:35
*/

func maxProfit2(prices []int) int {
	var ans int
	for i, price := range prices[1:] {
		if price-prices[i] > 0 {
			ans += price - prices[i]
		}
	}
	return ans
}
