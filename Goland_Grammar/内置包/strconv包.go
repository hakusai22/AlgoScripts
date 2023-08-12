package main

import (
	"fmt"
	"strconv"
)

// 主要用于字符串和基本类型的数据类型的转换
func main() {
	//字符串和整形数据不能放在一起  所以需要将100 整形转为字符串类型
	//+号在字符串中表示字符串的连接 在整形中表示数据的计算

	//string 转 bool类型
	s1 := "true" //字符串
	b, err := strconv.ParseBool(s1)
	if err != nil {
		fmt.Println(err) //打印错误信息
	}
	fmt.Printf("%T,%t", b, b) //bool,true

	//string 转int
	s1 = "100" //字符串
	b, err := strconv.ParseInt(s1, 10, 64)
	//10 表示s1要转的数据是10进制 64位
	if err != nil {
		fmt.Println(err) //打印错误信息
	}
	fmt.Printf("%T,%d", b, b) //int64,100

	//整形转为字符串
	s := strconv.Itoa(23)
	//字符串转为整形
	i, e := strconv.Atoi(s)
}
