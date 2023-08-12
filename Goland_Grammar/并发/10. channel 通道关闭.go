package main

import (
	"fmt"
)

/*
*
当发送者或者接收者把数据发生完毕，发送者可以关闭通道，通知接收方不会再有数据发送到channel上了然后发送方调用 close()方法关闭通道。
接收者可以获取来自通道数据时候额外的变量，来检测通道是否已经关闭。
*/
func main() {
	//创建一个通道用来传递数据
	ch1 := make(chan int)

	//通过子协程往通道中放数据
	go func() {
		fmt.Println("======子协程执行======")
		for i := 0; i < 10; i++ {
			ch1 <- i //往通道中放数据
		}
		close(ch1) //关闭通道
	}()

	//主协程通过for循环来获取通道中的所有数据
	for {
		v, ok := <-ch1 //获取通道的状态以及数据
		if !ok {
			fmt.Println("子协程已将通道关闭")
			break
		}
		fmt.Println("获取到的子协程数据为", v)
	}

	fmt.Println("主协程结束")
}
