package main

/*
   --idea
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/11/20 19:53
*/

func findMinimumOperations(s1 string, s2 string, s3 string) int {
	n := min(min(len(s1), len(s2)), min(len(s1), len(s3)))
	i := 0
	for i < n && s2[i] == s1[i] && s3[i] == s1[i] {
		i++
	}
	if i == 0 {
		return -1
	}
	return len(s1) + len(s2) + len(s3) - i*3
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
