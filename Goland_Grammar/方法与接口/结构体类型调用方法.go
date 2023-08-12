package main

/**
在Go语言中方法和函数类似，也可以认为方法是特殊类型的函数，
只不过方法限制了接收者，方法也可以说是包含了接收者的函数。
*/

import (
	"fmt"
)

// Role 创建一个结构体代表人物角色--任我行
type Role struct {
	Name    string  //姓名
	Ability string  //技能
	Level   int     //级别
	Kill    float64 //杀伤力
}

// Kungfu 创建一个方法,只要是Role结构体就能调用。
func (r Role) Kungfu() {
	fmt.Printf("我是:%s，我的武功:%s,已经练到%d级了，杀伤力%.1f\n", r.Name, r.Ability, r.Level, r.Kill)
}

func main() {
	//使用Role结构体创建一个角色代表任我行
	rwx := Role{"任我行", "吸星大法", 10, 9.9}
	rwx.Kungfu() //调用这个结构体的方法。
}
