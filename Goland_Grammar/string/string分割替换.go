/*
 * @Author: hakusai
 * @Date: 2023-05-17 16:41:18
 * @LastEditTime: 2023-05-17 16:46:13
 * @Description:
 */

package main

import (
	"fmt"
	"strings"
)

func case_14() {
	str := strings.Replace("go go go go 语言", "go", "goland", 2)
	fmt.Println(str)
}

func case_15() {
	array := strings.Split("dsaf asdf asdfa asdf", " ")
	fmt.Printf("替换后：%v   数据类型：%T", array, array)
}

func main() {
	case_14()
	case_15()
}
