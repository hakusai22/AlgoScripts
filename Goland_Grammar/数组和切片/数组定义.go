package main

import "fmt"

func main() {
	//数组定义
	var arr [5]int
	//数组访问使用下标来访问
	arr[0] = 1
	arr[1] = 2

	//通过下标直接获取数组数值
	fmt.Print(arr[2])

	fmt.Println("数组的长度为：", len(arr)) //数组中实际存储的数据量
	fmt.Println("数组的容量为：", cap(arr)) //容器中能够存储的最大数据量  因为数组是定长的 所以长度和容量是相同的
}
