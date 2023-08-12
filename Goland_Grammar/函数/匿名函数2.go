package main

import (
	"fmt"
)

func main() {
	res2 := opera(20, 12, add)
	fmt.Println(res2)

	//匿名函数作为回调函数直接写入参数中
	res3 := opera(2, 4, func(a, b int) int {
		return a + b
	})
	fmt.Println(res3)
}

func add(a, b int) int {
	return a + b
}
func reduce(a, b int) int {
	return a - b
}

// opera就叫做高阶函数
// fun 函数作为参数传递则fun在这里叫做回调函数
func opera(a, b int, fun func(int, int) int) int {
	fmt.Println(a, b, fun) //20 12 0x49a810A   第三个打印的是传入的函数体内存地址
	res := fun(a, b)       //fun 在这里作为回调函数 程序执行到此之后才完成调用
	return res
}
