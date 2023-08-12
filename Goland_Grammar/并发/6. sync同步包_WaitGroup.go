package main

import (
	"fmt"
	"sync"
)

/**
sync同步包，是Go语言提供的内置同步操作，保证数据统一的一些方法，
WaitGroup 等待一个goroutine的集合执行完成，也叫同步等待组，使用Add()方法，
来设置要等待一组goroutine 要执行的数量。用Done()方法来减去执行goroutine集合的数量。
使用Wait() 方法让主goroutine也就是main函数进入阻塞状态，等待其他的子goroutine执行结束后，main函数才会解除阻塞状态。
*/

// 创建一个同步等待组的对象
var wg sync.WaitGroup

func main() {
	wg.Add(3) //设置同步等待组的数量
	go Relief1()
	go Relief2()
	go Relief3()
	wg.Wait() //主goroutine进入阻塞状态
	fmt.Println("main end...")
}

func Relief1() {
	fmt.Println("func1...")
	wg.Done() //执行完成 同步等待数量减1
}
func Relief2() {
	defer wg.Done()
	fmt.Println("func2...")
}
func Relief3() {
	defer wg.Done() //推荐使用延时执行的方法来减去执行组的数量
	fmt.Println("func3...")
}
