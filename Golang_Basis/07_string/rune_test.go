package _7_string

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/08/28 17:06
*/

import (
	"fmt"
	"testing"
)

func TestName(t *testing.T) {
	main1()
}

func main1() {
	fmt.Println("go-algorithm", len("go-algorithm"))
	fmt.Println("go算法", len("go算法"))

	var str = "go算法"
	fmt.Println(str[:4])
	for k, v := range str {
		fmt.Printf("v type: %T\n", v)
		fmt.Println(v, k)
	}

	fmt.Println([]rune(str))
	fmt.Println([]byte(str))

	res := []rune(str)
	for _, re := range res {
		fmt.Println(string(re))
	}
	fmt.Println(len(res))
	fmt.Println(string(res[:4]))
}
