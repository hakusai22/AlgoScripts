package main

import "fmt"

func main() {
	//测试使用new方法新建切片
	slice1 := new([]int)
	fmt.Println(slice1) //输出的是一个地址  &[]

	//使用make创建切片
	slice2 := make([]int, 5)
	slice2[2] = 1
	fmt.Println(slice2[2:4])
	fmt.Println(slice2) //输出初始值都为0的数组， [0 0 0 0 0]
	//fmt.Println(slice1[0]) //结果出错 slice1是一个空指针 invalid operation: slice1[0] (type *[]int does not support indexing)
	fmt.Println(slice2[0]) //结果为 0 因为已经初始化了
}
