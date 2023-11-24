package _023_10

/*
   --idea
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/10/06 15:40
*/

func maxProfit3(prices []int) int {
	buy1, sell1, buy2, sell2 := -prices[0], 0, -prices[0], 0
	for _, price := range prices {
		buy1 = max(buy1, -price)
		sell1 = max(sell1, buy1+price)
		buy2 = max(buy2, sell1-price)
		sell2 = max(sell2, buy2+price)
	}
	return sell2
}
