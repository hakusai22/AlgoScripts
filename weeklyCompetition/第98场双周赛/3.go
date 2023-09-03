package 第98场双周赛

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/02/19 11:53
*/

func minImpossibleOR(nums []int) (ans int) {
	has := map[int]bool{}
	for _, v := range nums {
		has[v] = true
	}
	for i := 1; ; i <<= 1 {
		if !has[i] {
			return i
		}
	}
}
