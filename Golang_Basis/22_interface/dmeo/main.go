package main

import "fmt"

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/06 00:08
*/

func main() {
	var a int = 10
	funcName(a)

	var t interface{}
	switch t := t.(type) {
	default:
		fmt.Printf("unexpected type %T", t) // %T prints whatever type t has
	case bool:
		fmt.Printf("boolean %t\n", t) // t has type bool
	case int:
		fmt.Printf("integer %d\n", t) // t has type int
	case *bool:
		fmt.Printf("pointer to boolean %t\n", *t) // t has type *bool
	case *int:
		fmt.Printf("pointer to integer %d\n", *t) // t has type *int
	}
}

func funcName(a interface{}) string {
	value, ok := a.(string)
	if !ok {
		fmt.Println("not string")
		return ""
	}
	fmt.Println("value is", value)
	return value
}
