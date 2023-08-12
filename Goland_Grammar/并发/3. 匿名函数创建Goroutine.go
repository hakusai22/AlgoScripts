/*
 * @Author: hakusai
 * @Date: 2023-04-16 23:06:21
 * @LastEditTime: 2023-05-19 14:41:55
 * @Description:
 */
package main

import (
	"fmt"
)

func main() {
	go func() {
		fmt.Println("匿名函数创建goroutine执行")
	}()

	fmt.Println("主函数执行")
}
