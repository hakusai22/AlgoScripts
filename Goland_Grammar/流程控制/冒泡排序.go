package main

import "fmt"

func main() {
	values := []int{4, 3, 14, 85, 34, 27, 91, 95, 26, 12, 32}
	fmt.Println(values)
	BubblingASC(values)  //正序冒泡
	BubblingDESC(values) //倒序冒泡
}

// BubblingASC 冒泡排序 正序，大的靠后 小的靠前。
func BubblingASC(values []int) {
	for i := 0; i < len(values)-1; i++ {
		for j := i + 1; j < len(values); j++ {
			if values[i] > values[j] { //左右两边数据对比
				values[i], values[j] = values[j], values[i] //数据交换
			}
		}
	}
	fmt.Println(values)
}

// BubblingDESC 冒泡排序 倒序, 大的靠前 小的靠后。
func BubblingDESC(values []int) {
	for i := 0; i < len(values)-1; i++ {
		for j := i + 1; j < len(values); j++ {
			if values[i] < values[j] { //左右两边数据对比
				values[i], values[j] = values[j], values[i] //数据交换
			}
		}
	}
	fmt.Println(values)
}
