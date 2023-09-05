package main

import "fmt"

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/06 00:02
*/

func main() {
	Demo()
}

func Demo() {
	defer fmt.Println(1)
	defer fmt.Println(2)
	defer fmt.Println(3)
	defer fmt.Println(4)
}
