package main

import (
	"fmt"
)

/**
函数与方法的区别
1. 方法限制某个类别的行为,需要指定调用者。函数是一段独立的功能代码,可以直接调用。
2. 方法名称可以相同，只要接收者不同就可以，函数命名上不能冲突。
*/

// Haojiahuo 将好家伙 定义为int类型
type Haojiahuo int

// Clear 使用Clear方法将Haojiahuo的所有值清空
func (h Haojiahuo) Clear() bool {
	h = 0
	return h == 0
}

// Add 使用Add方法给Haojiahuo增加值
func (h Haojiahuo) Add(num int) int {
	return int(h) + num
}
func main() {
	var h Haojiahuo
	fmt.Println(h.Clear()) //调用清空方法
	fmt.Println(h.Add(2))  //调用添加方法加2
	fmt.Println(h.Clear()) //调用清空方法
	fmt.Println(h.Add(6))  //调用添加方法加6
	fmt.Println(h.Clear()) //调用清空方法
	fmt.Println(h)
}
