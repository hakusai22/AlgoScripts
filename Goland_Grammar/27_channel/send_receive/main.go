package main

import (
	"fmt"
	"time"
)

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/03 23:13
*/

func main() {
	//1
	messages := make(chan string)
	go func() { messages <- "ping" }()
	msg := <-messages
	fmt.Println(msg) // 输出ping

	//2
	messages2 := make(chan string, 2)
	messages2 <- "buffered"
	messages2 <- "channel"
	fmt.Println(<-messages2) // buffered
	fmt.Println(<-messages2) // channel

	//3
	done := make(chan bool, 1)
	go worker(done)
	<-done

	//4
	go person1()
	go person2()

	for {

	}
}

func worker(done chan bool) {
	fmt.Print("working...")
	time.Sleep(time.Second)
	fmt.Println("done")
	done <- true
}

var ch = make(chan int)

func Printer(str string) {
	for _, data := range str {
		fmt.Printf("%c", data)
		time.Sleep(time.Second)
	}
	fmt.Println("\n")
}

func person1() {
	Printer("Hello ")
	// 给通道写数据发送
	ch <- 666
}

func person2() {
	// 从通道中取数据，如果通道没有数据就会堵塞
	<-ch
	Printer("World")
}
