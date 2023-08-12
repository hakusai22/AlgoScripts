package main

import "fmt"

/**
数据如果按照数据类型划分
	基本类型:int、float、string、bool
	复合类型:array、slice、map、struct、pointer、function、chan
*/

/**
值类型：int、float、string、bool、array、struct 值传递是传递的数值本身，不是内存地，
将数据备份一份传给其他地址，本身不影响，如果修改不会影响原有数据。

引用类型: slice、pointer、map、chan 等都是引用类型。
引用传递因为存储的是内存地址，所以传递的时候则传递是内存地址，所以会出现多个变量引用同一个内存。
*/

func main() {
	//数组为值传递类型
	//定义一个数组 arr1
	arr1 := [4]int{1, 2, 3, 4}
	arr2 := arr1            //将arr1的值赋给arr2
	fmt.Println(arr1, arr2) //[1 2 3 4] [1 2 3 4]  输出结果 arr1与arr2相同，
	fmt.Println(arr1 == arr2)
	arr1[2] = 200           //修改arr1中下标为2的值
	fmt.Println(arr1, arr2) //[1 2 200 4] [1 2 3 4] 结果arr1中结果改变,arr2中不影响
	fmt.Println(arr1 == arr2)
	//说明只是将arr1中的值给了arr2 修改arr1中的值后并不影响arr2的值

	//切片是引用类型
	//定义一个切片 slice1
	slice1 := []int{1, 2, 3, 4}
	slice2 := slice1            //将slice1的地址引用到slice2
	fmt.Println(slice2, slice2) //[1 2 3 4] [1 2 3 4]   slice1输出结果 slice2输出指向slice1的结果，
	slice1[2] = 200             //修改slice1中下标为2的值
	fmt.Println(slice1, slice2) //[1 2 200 4] [1 2 200 4] 结果slice1中结果改变,因为修改的是同一份数据
	//说明只是将slice1中的值给了slice2 修改slice1中的值后引用地址用的是同一份 slice1 和slice2 同时修改

	fmt.Println(&slice1 == &slice2)
	fmt.Printf("%p,%p\n", slice1, slice2) //0xc000012520,0xc000012520
	//切片引用的底层数组是同一个 所以值为一个地址 是引用的底层数组的地址
	fmt.Printf("%p,%p\n", &slice1, &slice2) //0xc0000044a0,0xc0000044c0
	//切片本身的地址

	ints := make([]int, 4)
	ints2 := ints
	println(&ints == &ints2)
}
