package _2_process_control

import (
	"fmt"
	"testing"
)

func TestName2(t *testing.T) {
	var number int8 = 1
	switch number {
	case 0:
		fmt.Println("0")
	case 1:
		fmt.Println("1")
	case 2:
		fmt.Println("2")
	default:
		fmt.Println("default")
	}

	switch {
	case number == 0:
		fmt.Println("number == 0")
	case number == 1 || number < 2:
		fmt.Println("number == 1 || number < 2")
	case number == 2 && number > 0:
		fmt.Println("number == 2 && number > 0")
	default:
		fmt.Println("default")
	}

	// switch 语句还可以被用于 type-switch 来判断某个 interface 变量中实际存储的变量类型。
	var x interface{}
	//写法一：
	switch i := x.(type) { // 带初始化语句
	case nil:
		fmt.Printf(" x 的类型 :%T\r\n", i)
	case int:
		fmt.Printf("x 是 int 型")
	case float64:
		fmt.Printf("x 是 float64 型")
	case func(int) float64:
		fmt.Printf("x 是 func(int) 型")
	case bool, string:
		fmt.Printf("x 是 bool 或 string_test 型")
	default:
		fmt.Printf("未知型")
	}
}
