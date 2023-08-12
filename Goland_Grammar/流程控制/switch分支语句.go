package main

import "fmt"

/*
*
在switch 语句中，默认每个case后自带一个break，表示到此结束 不向下执行了，跳出整个switch。
fallthrough 表示强制执行后面的没有执行的case代码。
*/
func main() {
	//break 断开当前所有的执行 跳出整个switch
	n := 2
	switch n {
	case 1:
		fmt.Println("九阴真经")
		fmt.Println("九阴真经")
		fmt.Println("九阴真经")
	case 2:
		fmt.Println("葵花宝典")
		fmt.Println("葵花宝典")
		break
		fmt.Println("葵花宝典")
	case 3:
		fmt.Println("辟邪剑谱")
		fmt.Println("辟邪剑谱")
		fmt.Println("辟邪剑谱")
	}

	// fallthrough 穿透switch 当前case执行完了 继续执行下一case 不用匹配下一case是否符合直接执行
	//**fallthrough必须放在case最后一行
	m := 2
	switch m {
	case 1:
		fmt.Println("一月")
	case 2:
		fmt.Println("二月")
		fallthrough
	case 3:
		fmt.Println("三月")
	case 4:
		fmt.Println("四月")
	}
	//输出  二月 三月

}
