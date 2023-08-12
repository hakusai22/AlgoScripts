package main

import "fmt"

func main() {
	//copy(目标切片,数据源)  深拷贝数据函数
	s2 := []int{1, 2, 3, 4}
	s3 := []int{7, 8, 9}

	copy(s2, s3) //将s3拷贝到s2中
	fmt.Printf("%p,%p\n", s2, s3)
	fmt.Println(s2) //结果 [7 8 9 4]
	fmt.Println(s3) //结果 [7 8 9]

	copy(s3, s2[2:]) //将s2中下标为2的位置 到结束的值 拷贝到s3中
	fmt.Println(s2)  //结果 [1 2 3 4]
	fmt.Println(s3)  //结果 [3 4 9]

	copy(s3, s2)    //将s2拷贝到s3中
	fmt.Println(s2) //结果 [1 2 3 4]
	fmt.Println(s3) //结果 [1 2 3]

	//使用range循环将切片slice中的元素一个一个拷贝到切片s2中
	slice := []int{1, 2, 3, 4}
	ss2 := make([]int, 0)
	for _, v := range slice {
		ss2 = append(ss2, v)
	}
	fmt.Println(slice) //结果 [1 2 3 4]
	fmt.Println(ss2)   //结果 [1 2 3 4]
	fmt.Printf("%p,%p\n", slice, ss2)
}
