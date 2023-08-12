/*
 * @Author: hakusai
 * @Date: 2023-04-16 23:06:21
 * @LastEditTime: 2023-05-19 14:42:04
 * @Description:
 */
package main

import (
	"fmt"
	"runtime"
	"time"
)

func main() {
	//获取当前GOROOT目录
	fmt.Println("GOROOT:", runtime.GOROOT())
	//获取当前操作系统
	fmt.Println("操作系统:", runtime.GOOS)
	//获取当前逻辑CPU数量
	fmt.Println("逻辑CPU数量：", runtime.NumCPU())

	//设置最大的可同时使用的CPU核数  取逻辑cpu数量
	n := runtime.GOMAXPROCS(runtime.NumCPU())
	fmt.Println(n) //一般在使用之前就将cpu数量设置好 所以最好放在init函数内执行

	//goexit 终止当前goroutine
	//创建一个goroutine
	go func() {
		fmt.Println("start...")
		// 如果调用runtime.Goexit()函数之后，会立即停止当前goroutine，其他的goroutine不会受影响。
		runtime.Goexit() //终止当前goroutine
		fmt.Println("end...")
	}()
	time.Sleep(3 * time.Second) //主goroutine 休眠3秒 让子goroutine执行完
	fmt.Println("main_end...")
}
