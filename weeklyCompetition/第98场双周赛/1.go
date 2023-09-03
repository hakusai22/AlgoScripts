package 第98场双周赛

import (
	"strconv"
	"strings"
)

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/02/19 11:53
*/

func minMaxDifference(num int) (ans int) {
	// 字符串转int：Atoi()
	// int转字符串：Itoa()
	s := strconv.Itoa(num)
	mx := 0
	mi := int(1e18)
	for _, c := range s {
		t := strings.ReplaceAll(s, string(c), "9")
		v, _ := strconv.Atoi(t)
		mx = max(mx, v)
		t = strings.ReplaceAll(s, string(c), "0")
		v, _ = strconv.Atoi(t)
		mi = min(mi, v)
	}
	ans = mx - mi
	return
}

func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}
