package main

import "fmt"

func main() {
	//方法一 获取切片指定位置的值 重新赋值给当前切片
	slice := []int{1, 2, 3, 4}
	fmt.Printf("%p\n", slice)

	slice = slice[1:] //删除切片中开头1个元素  结果 [2,3,4]
	fmt.Println(slice)
	fmt.Printf("%p\n", slice)

	//方法二 使用append不会改变当前切片的内存地址
	slice = append(slice[:0], slice[1:]...) // 删除开头1个元素
	fmt.Println(slice)
	fmt.Printf("%p\n", slice)

	slice11 := []int{1, 2, 3, 4}
	i := 2                                        // 要删除的下标为2
	slice = append(slice11[:i], slice11[i+1:]...) // 删除中间1个元素
	fmt.Println(slice11)

	slice22 := []int{1, 2, 3, 4}
	slice22 = slice22[:len(slice22)-2] // 删除最后2个元素
	fmt.Println(slice22)               //结果 [1,2]//结果[1 2 4]
}
