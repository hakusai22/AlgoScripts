package _3_oop

import (
	"fmt"
	"testing"
)

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/16 01:30
   @题目     :
   @参考     :
   @时间复杂度:
*/

// Sayer 接口
type Sayer interface {
	say()
}

// Mover 接口
type Mover interface {
	move()
}

// 一个类型实现多个接口
type dog struct {
	name string
}

// 实现Sayer接口
func (d dog) say() {
	fmt.Printf("%s会叫汪汪汪\n", d.name)
}

func (d dog) move() {
	fmt.Println("狗会动")
}

func (d *dog) move2() {
	fmt.Println("狗会动")
}

var x Mover

func TestName(t *testing.T) {
	var wangcai = dog{} // 旺财是dog类型
	x = wangcai         // x可以接收dog类型
	var fugui = &dog{}  // 富贵是*dog类型
	x = fugui           // x可以接收*dog类型
	x.move()
}

func TestName2(t *testing.T) {
	var wangcai = dog{} // 旺财是dog类型
	x = wangcai         // x不可以接收dog类型
	var fugui = &dog{}  // 富贵是*dog类型
	x = fugui           // x可以接收*dog类型
}
