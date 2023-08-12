package main

import "fmt"

func main() {
	//默认情况下 数组中每个元素初始化时候 根据元素的类型 对应该数据类型的零值，
	arr1 := [3]int{1, 2}
	fmt.Println(arr1[2]) //下标为2的元素没有默认取int类型的零值
	fmt.Println(len(arr1))
	fmt.Println(cap(arr1))

	//数组创建方式1 创建时 直接将值赋到数组里
	arr2 := [5]int{1, 2, 3, 4} //值可以少 默认是0  但是不能超过定长

	fmt.Println(arr2)
	//在指定位置上存储值
	arr3 := [5]int{1: 2, 3: 5} //在下标为1的位置存储2，在下标为3的位置存储5
	fmt.Println(arr3)

	//长度可以用...代替  根据数值长度程序自动填充数值的大小
	arr4 := [...]int{1, 2, 3, 4}
	fmt.Println(arr4)

	//简短声明方式
	arr5 := [...]int{2: 3, 6: 3} //在固定位置存储固定的值
	fmt.Println(arr5)

}
