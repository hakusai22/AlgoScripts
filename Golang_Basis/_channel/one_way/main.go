package main

import "fmt"

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/06 00:42
*/

func main() {
	//var ch1 chan int       // ch1是一个正常的channel，是双向的
	//var ch2 chan<- float64 // ch2是单向channel，只用于写float64数据
	//var ch3 <-chan int     // ch3是单向channel，只用于读int数据

	c := make(chan int, 3)
	var send chan<- int = c // send-only
	var recv <-chan int = c // receive-only
	send <- 1
	//<-send //invalid operation: <-send (receive from send-only type chan<- int)
	<-recv
	//recv <- 2 //invalid operation: recv <- 2 (send to receive-only type <-chan int)

	//不能将单向 channel 转换为普通 channel

	c2 := make(chan int) //   chan   //读写

	go counter(c2) //生产者
	printer(c2)    //消费者

	fmt.Println("done")
}

// chan<- //只写
func counter(out chan<- int) {
	defer close(out)
	for i := 0; i < 5; i++ {
		out <- i //如果对方不读 会阻塞
	}
}

// <-chan //只读
func printer(in <-chan int) {
	for num := range in {
		fmt.Println(num)
	}
}
