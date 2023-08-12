package main

import "fmt"

func main() {
	//声明一个二维数组
	var arr [3][8]int
	//给二维数组赋值
	arr[0] = [8]int{1, 2, 3, 4, 5, 6, 7, 8}
	//打印结果
	fmt.Println(arr) // [[1 2 3 4 5 6 7 8] [0 0 0 0 0 0 0 0] [0 0 0 0 0 0 0 0]]
	//也可以通过下标给指定的索引赋值
	arr[1][3] = 9
	fmt.Println(arr) // [[1 2 3 4 5 6 7 8] [0 0 0 9 0 0 0 0] [0 0 0 0 0 0 0 0]]
}
