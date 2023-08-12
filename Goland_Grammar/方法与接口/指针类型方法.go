package main

import (
	"fmt"
)

// 方法的接收者可以是结构体类型，也可以是一个值，或者是一个指针类型。
func main() {
	rwx := &Role{"任我行", "吸星大法", 8, 10}
	rwx.Kungfu() //使用Role该类型的指针调用方法

	zwj := &Role{"张无记", "九娘神功", 9, 12}
	zwj.Kungfu2() //调用指针类型方法
}

// Role 创建一个结构体代表人物角色--任我行或者张无忌
type Role struct {
	Name    string  //姓名
	Ability string  //技能
	Level   int     //级别
	Kill    float64 //杀伤力
}

func (r Role) Kungfu() {
	fmt.Printf("我是:%s，我的武功:%s,已经练到%d级了，杀伤力%.1f\n", r.Name, r.Ability, r.Level, r.Kill)
}

// Kungfu2 指针类型方法
func (r *Role) Kungfu2() {
	fmt.Printf("我是:%s，我的武功:%s,已经练到%d级了，杀伤力%.1f\n", r.Name, r.Ability, r.Level, r.Kill)
}
