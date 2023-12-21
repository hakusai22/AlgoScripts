package main

import "fmt"

/*
   --idea
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/12/21 22:06
*/

func main() {
	s1 := make([]int, 2)
	mdSlice1(s1)
	fmt.Println(s1)
	var s2 []int
	mdSlice2(s2)
	fmt.Println(s2)
}

func mdSlice1(s []int) {
	s[0] = 1
	s[1] = 2
}

func mdSlice2(s []int) {
	s = make([]int, 2)
	s[0] = 1
	s[1] = 2
}
