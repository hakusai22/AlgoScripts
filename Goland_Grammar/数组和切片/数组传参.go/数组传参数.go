/*
 * @Author: hakusai
 * @Date: 2023-05-14 13:06:23
 * @LastEditTime: 2023-05-14 13:11:33
 */
package main

import "fmt"

func testArr01(arr []int) { //形参未指定大小
	arr[0]++
}
func testArr02(arr [5]int) { //形参指定大小
	arr[0]++
}
func testArr03(arr *[5]int) { //使用指针方式，也就是引用传递
	arr[0]++
}

func main() {
	var arr = [5]int{0, 2, 3, 17, 50}
	testArr01(arr[:]) //切片方式传递（常用）
	for i := 0; i < len(arr); i++ {
		fmt.Printf("%d ", arr[i])
	}
	fmt.Println()

	testArr02(arr) //数组名方式传递,此时传递的是副本，并不会改变原数组
	for i := 0; i < len(arr); i++ {
		fmt.Printf("%d ", arr[i])
	}
	fmt.Println()

	testArr03(&arr) //指针方式传递，会改变原数组
	for i := 0; i < len(arr); i++ {
		fmt.Printf("%d ", arr[i])
	}
	fmt.Println()
}
