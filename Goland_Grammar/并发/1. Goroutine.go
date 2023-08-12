/*
 * @Author: hakusai
 * @Date: 2023-04-16 23:06:21
 * @LastEditTime: 2023-05-19 14:41:16
 * @Description:
 */
package main

import (
	"fmt"
	"time"
)

func main() {
	go testgo() //使用关键字go调用函数或者方法 开启一个goroutine
	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}
	fmt.Println("main 函数结束")
	time.Sleep(3000 * time.Millisecond) //加上休眠让主程序休眠3秒钟。

}

// 自定义函数
func testgo() {
	for i := 0; i < 10; i++ {
		fmt.Println("测试goroutine", i)
	}
}
