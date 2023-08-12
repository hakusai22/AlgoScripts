package main

import (
	"fmt"
	"sync"
	"time"
	// "runtime"
)

// 创建一把读写锁 可以是他的指针类型
var rwmutex sync.RWMutex

var wg sync.WaitGroup

/*
*
读写锁的控制规则是，他允许任意多个读操作同时进行，
但是只允许一个写操作进行，并且在某一个写操作的时候不允许读操作进行。
*/
func main() {
	wg.Add(3)
	go ReadTest(1)
	go WriteTest(2)
	go ReadTest(3)
	wg.Wait()
	fmt.Println("======main结束======")
}

// 读取数据的方法
func ReadTest(i int) {
	defer wg.Done()
	fmt.Println("======准备读取数据======", i)
	rwmutex.RLock() //读上锁
	fmt.Println("======正在读取...", i)
	rwmutex.RUnlock() //读取操作解锁
	fmt.Println("======读取结束======", i)
}

func WriteTest(i int) {
	defer wg.Done()
	fmt.Println("======开始写数据======", i)
	rwmutex.Lock() //写操作上锁
	fmt.Println("======正写数据...", i)
	time.Sleep(1 * time.Second)
	rwmutex.Unlock() //写操作解锁
	fmt.Println("======写操作结束======", i)
}
