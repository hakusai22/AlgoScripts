package main

import (
	"fmt"
	"time"
)

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/06 00:34
*/

func main() {
	c := make(chan int, 3) //带缓冲的通道

	//内置函数 len 返回未被读取的缓冲元素数量， cap 返回缓冲区大小
	fmt.Printf("len(c)=%d, cap(c)=%d\n", len(c), cap(c))

	go func() {
		defer fmt.Println("子go程结束")

		for i := 0; i < 3; i++ {
			c <- i
			fmt.Printf("子go程正在运行[%d]: len(c)=%d, cap(c)=%d\n", i, len(c), cap(c))
		}
	}()

	time.Sleep(2 * time.Second) //延时2s
	for i := 0; i < 3; i++ {
		num := <-c //从c中接收数据，并赋值给num
		fmt.Println("num = ", num)
	}
	fmt.Println("main进程结束")
}
