package _16_1126_3

/*
--idea
-*- coding: utf-8 -*-
@Author  : hakusai22
@Time    : 2023/11/26 23:26
*/
func minChanges(s string) (ans int) {
	for i := 0; i < len(s); i += 2 {
		if s[i] != s[i+1] {
			ans++
		}
	}
	return
}
