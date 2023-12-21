package main

import "fmt"

/*
   --idea
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/12/21 22:04
*/

func main() {
	m1 := make(map[int]int)
	mdMap1(m1)
	fmt.Println(m1)

	var m2 map[int]int
	mdMap2(m2)
	fmt.Println(m2)
}

// m1 中，当调用 mdMap 方法时重新开辟了内存，将 m 的内容，
// 也就是 map 的地址拷贝入了 m'，所以此时当操作 map 时，
// m 和 m' 所指向的内存为同一块，就导致 m 的 map 发生了改变。
func mdMap1(m map[int]int) {
	m[1] = 100
	m[2] = 200
}

// 而在 m2 中，在调用 mdMap 之前，m 并未分配内存，
// 也就是说并未指向任何的 map 内存区域。
// 从未导致 m' 的 map 修改不能反馈到 m 上。
func mdMap2(m map[int]int) {
	m = make(map[int]int)
	m[1] = 100
	m[2] = 200
}
