package main

import (
	"fmt"
)

func main() {
	//创建一个普通的数组
	arr := [3]int{1, 2, 3}
	fmt.Println(arr)

	//创建一个指针 用来存储数组的地址 即：数组指针
	var p *[3]int
	p = &arr       //将数组arr的地址，存储到数组指针p上。
	fmt.Println(p) //数组的指针 &[1 2 3] 后面跟数组的内容

	//获取数组指针中的具体数据 和数组指针自己的地址
	fmt.Println(*p) //指针所对应的数组的值
	fmt.Println(&p) //该指针自己的地址0xc000006030

	//修改数组指针中的数据
	(*p)[0] = 200
	fmt.Println(arr) //修改数组中下标为0的值为200   结果为：[200 2 3]

	//简化写法
	p[1] = 210       //意义同上修改下标为1的数据
	fmt.Println(arr) //结果： [200 210 3]
}
