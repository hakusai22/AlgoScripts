package main

import (
	"Go_Study/Goland_Grammar/20_package/model"
	"fmt"
)

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/08/14 16:36
*/

func main() {
	//创建Student实例
	// var stu = model.Student{
	// 	Name :"tom",
	// 	Score : 78.9,
	// }

	//定student结构体是首字母小写，我们可以通过工厂模式来解决
	var stu = model.NewStudent("tom~", 98.8)

	fmt.Println(stu)                                          //&{tom~ 98.8}
	fmt.Println("name=", stu.Name, " score=", stu.GetScore()) //name= tom~  score= 98.8
}
