package 第338场周赛

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/04/03 14:41
*/

func kItemsWithMaximumSum(numOnes int, numZeros int, numNegOnes int, k int) (ans int) {
	a := []int{}
	for i := 0; i < numOnes; i++ {
		a = append(a, 1)
	}
	for i := 0; i < numZeros; i++ {
		a = append(a, 0)
	}
	for i := 0; i < numNegOnes; i++ {
		a = append(a, -1)
	}

	sum := 0
	for _, v := range a[:k] {
		sum += v
	}
	ans = sum
	return
}
