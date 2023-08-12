package main

import (
	"fmt"
)

func main() {
	defer test1(1) //第一个被defer的，函数后执行
	defer test1(2) //第二个被defer的，函数先执行
	test1(3)       //没有defer的函数，第一次执行

	//执行结果
	//3
	//2
	//1
}

func test1(s int) {
	fmt.Println(s)
}
