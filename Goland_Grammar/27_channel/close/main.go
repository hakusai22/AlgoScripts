package main

import (
	"fmt"
	"time"
)

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/03 20:26
*/

func main() {
	//1
	queue := make(chan string, 2)
	queue <- "one"
	queue <- "two"
	close(queue)

	for elem := range queue {
		fmt.Println(elem)
	}

	//2
	receive()
}

func receive() {
	ch := make(chan int, 100)
	for i := 0; i < 10; i++ {
		ch <- i
	}
	// ch <- 0
	close(ch) // !!!!!!

	for {
		i, ok := <-ch
		fmt.Println(i, ok)
		time.Sleep(time.Second)
	}
}
