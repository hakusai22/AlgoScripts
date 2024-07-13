package _73_1126_2

/*
--idea
-*- coding: utf-8 -*-
@Author  : hakusai22
@Time    : 2023/11/26 18:09
*/
func areSimilar(mat [][]int, k int) bool {
	n := len(mat[0])
	k %= n
	if k == 0 {
		return true
	}
	//for _, r := range mat {
	//	if !slices.Equal(r, append(r[k:], r[:k]...)) { // go 1.21引入slices
	//		return false
	//	}
	//}
	return true
}
