package main

import "fmt"

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/08/13 21:45
*/

// =是赋值变量，:=是定义变量。

// 指针学习
func main() {
	var num = 10
	fmt.Println("num的地址:", &num) //num的地址： 0x1400009c018

	//1. ptr 是一个指针变量
	//2. ptr 类型是 *int
	//3. ptr本身的值为 &num （num的地址）
	var ptr = &num
	fmt.Println("ptr的值:", ptr)   //ptr的值: 0x1400009c018
	fmt.Println("ptr的地址:", &ptr) //ptr的地址: 0xc000006030

	fmt.Println("ptr指向的值:", *ptr) //ptr指向的值: 10

	*ptr = 666
	fmt.Println("num的值:", num) //num的值: 666

}
