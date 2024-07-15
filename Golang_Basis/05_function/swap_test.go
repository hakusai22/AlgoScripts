package _05_function

import (
	"fmt"
	"testing"
)

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/05 23:58
*/

func TestName(t *testing.T) {
	main2()
}

/* 定义相互交换值的函数 */
func swap(x, y int) int {
	var temp int

	temp = x /* 保存 x 的值 */
	x = y    /* 将 y 值赋给 x */
	y = temp /* 将 temp 值赋给 y*/

	return temp
}

/* 定义交换值函数*/
func swap2(x *int, y *int) {
	var temp int
	temp = *x /* 保持 x 地址上的值 */
	*x = *y   /* 将 y 值赋给 x */
	*y = temp /* 将 temp 值赋给 y */
}

func main2() {
	var a int = 100
	var b int = 200
	fmt.Printf("a: %d", a)
	fmt.Printf("b: %d", b)
	swap(a, b)
	fmt.Printf("a: %d", a)
	fmt.Printf("b: %d", b)

	/* 调用 swap() 函数
	 * &a 指向 a 指针，a 变量的地址
	 * &b 指向 b 指针，b 变量的地址
	 */
	swap2(&a, &b)

	fmt.Printf("交换后，a 的值 : %d\n", a)
	fmt.Printf("交换后，b 的值 : %d\n", b)
}
