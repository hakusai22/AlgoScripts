package main

import (
	"fmt"
)

func main() {
	x := 2
	test()
	fmt.Println(x)

	i := 2
	x2 := 20
	fmt.Println(x2) //if语句内部定义的x
	fmt.Println(i)  //if内部定义的i  if之外就不能访问了
}

// 函数外部定义全局变量
// 全局变量不支持简短定义方法 n:=0
var n = 3 //全局变量可以随意被修改 如果不想被修改可以定义为常量

func test() {
	//fmt.Print(x) //undefined: x  未定义 x是main函数中定义的变量 所以不能访问
	fmt.Println(n) //全局变量 任何地方都可以访问
}
