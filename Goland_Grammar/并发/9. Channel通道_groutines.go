package main

import (
	"fmt"
)

/**
当存在多个goroutine要传递某一个数据时，可以把这个数据封装成一个对象，
然后把对象的指针传入channel通道中，另一个goroutine 从通道中读取这个指针。
同一时间只允许一个goroutine访问channel通道里面的数据。
所以go就是把数据放在了通道中来传递，而不是共享内存来传递。
*/

func main() {
	//通道的声明
	var channel1 chan int
	//如果通道时nil 则要通过make创建通道
	channel1 = make(chan int)
	fmt.Println(channel1)

	var channle chan int
	fmt.Printf("通道的数据类型:%T,通道的值:%v\n", channle, channle) //

	if channle == nil {
		channle = make(chan int)
		fmt.Printf("通过make创建的通道数据类型:%T,通道的值:%v,\n", channle, channle)
		//make创建后 通道的值为 0xc00005c060 也就是一个内存地址
		//所以channel 是一个引用类型的数据
	}

	/**
	不管是发送数据还是获取数据， 他们都是阻塞的，
	当一个goroutine 向另一个goroutine发送数据的时候，他就是阻塞的，直到有另外一个goroutine来取数据，则解除阻塞。
	相反的 读取数据也是阻塞的，直到另一个goroutine向他来写数据来解除阻塞。channel 本身就是同步的。
	也就是同一时间只允许一条goroutine来操作。要使用通道最少有两个goroutine来操作。一个goroutine是用不到channel的。
	*/
	ch1 := make(chan int)
	go func() {
		fmt.Println("======子协程执行======")
		data := <-ch1 //从通道中读取数据
		fmt.Println("读取到通道中的数据是:", data)
	}()
	ch1 <- 10 //往通道里放数据
	fmt.Println("======主协程结束======")
}
