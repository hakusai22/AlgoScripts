package hashTable

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/09 14:16
*/

func minSteps(s string, t string) int {
	m := map[rune]int{}
	for _, v := range s {
		m[v]++
	}
	for _, v := range t {
		m[v]--
	}
	ans := 0
	for _, v := range m {
		if v > 0 {
			ans += v
		}
	}
	return ans
}
