package main

import (
	"fmt"
	"os"
)

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/08/14 17:48
*/

//概念说明: file 的叫法
//1. file 叫 file对象
//2. file 叫 file指针
//3. file 叫 file 文件句柄

func main() {
	//打开文件
	file, err := os.Open("/Users/yinpeng/GoWorkSpace/Go_Study/Golang_Basis/07_file_operate/open_close/1.txt")
	if err != nil {
		fmt.Println("open file err=", err)
	}

	//输出下文件，看看文件是什么, 看出file 就是一个指针 *File
	fmt.Printf("file= %v", file) //file=&{0xc000090780}

}
