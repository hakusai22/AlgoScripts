package main

import (
	"encoding/json"
	"fmt"
)

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/03 23:57
*/

type Person struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
}

func main() {
	var person Person
	jsonStr := `{
    "name":"hello", "age":1 }`
	// 注意这里要传递person的指针，不然person不会改变
	err := json.Unmarshal([]byte(jsonStr), &person)
	if err != nil {
		fmt.Println("err :", err)
		return
	}
	fmt.Println("person : ", person)
}
