package main

import "fmt"

func main() {
	arr := [5]int{1, 2, 3, 4, 5}
	//range方式循环数组
	for index, value := range arr {
		fmt.Println(index, value)
	}

	//for循环
	for i := 0; i < len(arr); i++ {
		fmt.Println(arr[i])
	}
}
