package _3_oop

import (
	"fmt"
	"testing"
)

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/16 01:33
   @题目     :
   @参考     :
   @时间复杂度:
*/

// 接口嵌套 嵌套得到的接口的使用与普通接口一样
type animal interface {
	Sayer
	Mover
}

type cat struct {
	name string
}

func (c cat) say() {
	fmt.Println("喵喵喵")
}

func (c cat) move() {
	fmt.Println("猫会动")
}

func TestName3(t *testing.T) {
	var x animal
	x = cat{name: "花花"}
	x.move()
	x.say()
}
