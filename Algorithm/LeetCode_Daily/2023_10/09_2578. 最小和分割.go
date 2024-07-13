package _023_10

import (
	"sort"
	"strconv"
)

/*
--idea
-*- coding: utf-8 -*-
@Author  : hakusai22
@Time    : 2023/11/14 23:31
*/
func splitNum(num int) int {
	s := []byte(strconv.Itoa(num))
	sort.Slice(s, func(i, j int) bool { return s[i] < s[j] })
	a := [2]int{}
	for i, c := range s {
		a[i%2] = a[i%2]*10 + int(c-'0') // 按照奇偶下标分组
	}
	return a[0] + a[1]
}
