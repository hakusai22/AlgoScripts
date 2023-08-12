package main

import "fmt"

func main() {
	//for 标准写法
	for i := 0; i <= 5; i++ {
		fmt.Println(i, "次执行")
	}

	//for其他写法  初始化可以放for循环外 表达式2写在循环体内部
	i := 1
	for i <= 5 {
		fmt.Println("循环体")
		i++
	}

	// 如果表达式2 条件判断省略 则进入死循环模式
	for {
		fmt.Println("....")
	}
}
