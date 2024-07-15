package _3_oop

import (
	"fmt"
	"testing"
)

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/16 01:35
   @题目     :
   @参考     :
   @时间复杂度:
*/

// 空接口作为函数参数
func show(a interface{}) {
	fmt.Printf("type:%T value:%v\n", a, a)
}

func TestName4(t *testing.T) {
	// 定义一个空接口x
	var x interface{}
	s := "pprof.cn"
	x = s
	fmt.Printf("type:%T value:%v\n", x, x)
	i := 100
	x = i
	fmt.Printf("type:%T value:%v\n", x, x)
	b := true
	x = b
	fmt.Printf("type:%T value:%v\n", x, x)

	// 空接口作为map值 使用空接口实现可以保存任意值的字典。
	var studentInfo = make(map[string]interface{})
	studentInfo["name"] = "李白"
	studentInfo["age"] = 18
	studentInfo["married"] = false
	fmt.Println(studentInfo)

	x = "pprof.cn"
	v, ok := x.(string)
	if ok {
		fmt.Println(v)
	} else {
		fmt.Println("类型断言失败")
	}
}
