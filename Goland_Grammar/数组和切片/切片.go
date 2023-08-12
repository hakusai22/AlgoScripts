package main

import "fmt"

func main() {
	//使用make函数来创建切片
	slice1 := make([]int, 3, 5)           //长度为3 容量为5  容量如果省略 则默认与长度相等也为3
	fmt.Println(slice1)                   //[0,0,0]
	fmt.Println(len(slice1), cap(slice1)) //长度3,容量5

	//使用append() 给切片末尾追加元素
	var slice []int
	slice = append(slice, 1, 2, 3)
	fmt.Println(slice) // [1, 2, 3]

	//使用make函数创建切片
	s1 := make([]int, 0, 5)
	fmt.Println(s1) // [] 打印空的切片
	s1 = append(s1, 1, 2)
	fmt.Println(s1) // [1,2]
	//因为切片可以扩容  所以定义容量为5 但是可以加无数个数值
	s1 = append(s1, 3, 4, 5, 6, 7)
	fmt.Println(s1) // [1,2,3,4,5,6,7]

	//添加一组切片到另一切片中
	s2 := make([]int, 0, 3)
	s2 = append(s2, s1...) //...表示将另一个切片数组完整加入到当前切片中
}
