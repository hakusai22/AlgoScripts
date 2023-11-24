package main

/*
   --idea
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/11/20 19:57
*/
func minimumSteps(s string) (ans int64) {
	cnt := 0
	for _, c := range s {
		if c == '1' {
			cnt++
		} else {
			ans += int64(cnt)
		}
	}
	return
}
