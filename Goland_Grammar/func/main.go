package main

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/08/12 08:32
*/

import (
	"fmt"
)

// User 结构体
type User struct {
	Name  string
	Email string
}

type Manager struct {
	User
	title string
}

func (self *User) ToString() string { // receiver = &(Manager.User)
	return fmt.Sprintf("User: %p, %v", self, self)
}

func (self *Manager) ToString() string {
	return fmt.Sprintf("Manager: %p, %v", self, self)
}

// Notify 方法
func (u User) Notify() {
	fmt.Printf("%v : %v \n", u.Name, u.Email)
}
func main() {
	test1()
	test2()
	test3()
}

func test1() {
	// 值类型调用方法
	u1 := User{"golang", "golang@golang.com"}
	u1.Notify()
	// 指针类型调用方法
	u2 := User{"go", "go@go.com"}
	u3 := &u2
	u3.Notify()
}

type Data struct {
	x int
}

func (self Data) ValueTest() { // func ValueTest(self Data);
	fmt.Printf("Value: %p\n", &self)
}

func (self *Data) PointerTest() { // func PointerTest(self *Data);
	fmt.Printf("Pointer: %p\n", self)
}

func test2() {
	d := Data{}
	p := &d
	fmt.Printf("Data: %p\n", p)

	d.ValueTest()   // ValueTest(d)
	d.PointerTest() // PointerTest(&d)

	p.ValueTest()   // ValueTest(*p)
	p.PointerTest() // PointerTest(p)
}

func test3() {
	m := Manager{User{"asdf", "Tom"}, "admin"}
	fmt.Printf("Manager: %p\n", &m)
	fmt.Println(m.ToString())
	fmt.Println(m.User.ToString())
}
