package main

import (
	"fmt"
)

/*
   --idea
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/12/21 21:55
*/

func main() {
	s := []int{}
	for i := 0; i < 4098; i++ {
		s = append(s, i)
		fmt.Println(len(s), cap(s))
		fmt.Printf("11:%T", s)
	}
	fmt.Printf("11:%T", s)

}
