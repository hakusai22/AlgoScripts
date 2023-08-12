package main

import (
	"fmt"
)

func main() {
	//函数默认为指针 只是不需要用 *
	a := fun1
	fmt.Println(a) //0x49c670 函数默认为指针类型
	a1 := fun1()
	fmt.Printf("a1的类型：%T,a1的地址是%p 数值为%v \n", a1, &a1, a1) //[]int,a1的地址是0xc0000044c0 数值为[1 2 3]

	a2 := fun2()
	fmt.Printf("a2的类型：%T,a2的地址是%p 数值为%v \n", a2, &a2, a2) //*[]int,a1的地址是0xc000006030 数值为&[1 2 3 4]
	fmt.Printf("a2的值为：%p\n", a2)                          //0xc000004520 指针函数返回的就是指针
}

// 一般函数
func fun1() []int {
	c := []int{1, 2, 3}
	return c
}

// 指针函数 返回指针
func fun2() *[]int {
	c := []int{1, 2, 3, 4}
	fmt.Printf("c的地址为%p：\n", &c) //0xc000004520
	return &c
}
