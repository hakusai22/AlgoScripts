package main

import "fmt"

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/08/13 22:04
*/

func main() {
	const (
		Bool = iota //表示赋值为0，后面的依次递增
		Int
		Int8
		Int16
		Int32
		Int64
		Uint
		Uint8
		Uint16
		Uint32
		Uint64
		Uintptr
		Float32
		Float64
		Complex64
		Complex128
		Array
		Chan
		Func
		Interface
		Map
		Ptr
		Slice
		String
		Struct
		UnsafePointer
	)
	fmt.Println(Bool, Int, Int8, Int16, Map)
}
