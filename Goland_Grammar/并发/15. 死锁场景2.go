package main

import (
	"fmt"
)

func main() {
	c := make(chan int)
	c <- 100 //向通道中写入数据
	a := <-c //读取通道中的数据
	fmt.Println(a)
}
