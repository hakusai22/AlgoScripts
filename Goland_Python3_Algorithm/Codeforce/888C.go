package main

import (
	"bufio"
	. "fmt"
	"os"
)

/*
   --idea
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/12/11 15:46
*/

func main() {
	s := ""
	Fscan(bufio.NewReader(os.Stdin), &s)
	pos := [26][]int{}
	for i, b := range s {
		b -= 'a'
		pos[b] = append(pos[b], i)
	}
	n := len(s)
	ans := n
	for _, ps := range pos {
		ps = append(append([]int{-1}, ps...), n)
		maxD := 0
		for i := 1; i < len(ps); i++ {
			maxD = max(maxD, ps[i]-ps[i-1])
		}
		ans = min(ans, maxD)
	}
	Fprint(os.Stdout, ans)
}

func min(a, b int) int {
	if b < a {
		return b
	}
	return a
}
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
