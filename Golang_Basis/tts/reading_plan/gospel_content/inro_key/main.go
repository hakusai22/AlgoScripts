package main

import (
	"fmt"
	"strconv"
)

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/09/12 16:15
    @题目     :
    @参考     :
    @时间复杂度:
    @空间复杂度:

 数据范围:

*/

func main() {
	str := "peace_amidst_stress_intro_"
	for i := 1; i < 7; i++ {
		fmt.Println(str + strconv.Itoa(i))
	}
}
