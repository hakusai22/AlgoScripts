package main

import (
	"fmt"
)

func main() {
	//定义一个缓冲区大小为5的通道
	ch1 := make(chan int, 5)
	ch1 <- 1 //向缓冲区放入数据1 因为缓冲区的大小为5 放入一个1之后 还有四个空的缓冲区  所以还未阻塞
	ch1 <- 2
	ch1 <- 3
	ch1 <- 4
	ch1 <- 5 //此时缓冲区已经满 如果再加入 则会进入阻塞状态
	//继续添加时会造成死锁 因为缓冲区满了 一直没有读取
	//ch1 <- 6 //fatal error: all goroutines are asleep - deadlock!
	fmt.Println("main end")

	//定义一个缓冲区大小为5的通道
	ch2 := make(chan int, 5)

	//开启子协程写入数据
	go func() {
		for i := 0; i < 10; i++ {
			ch2 <- i
			fmt.Println("子协程写入数据：", i)
		}
		close(ch2) //关闭通道
	}()

	//主协程读取数据
	for {
		v, ok := <-ch2
		if !ok {
			fmt.Println("读取结束", ok)
			break
		}
		fmt.Println("主协程读取到的数据为：", v)
	}

	fmt.Println("主协程结束")
}
