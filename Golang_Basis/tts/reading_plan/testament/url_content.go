package main

import (
	"fmt"
	"os"
)

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/09/10 11:38
    @题目     :
    @参考     :
    @时间复杂度:
    @空间复杂度:

 数据范围:

*/

func main() {
	DOMAIN_FF := os.Getenv("DOMAIN_FF")
	str := DOMAIN_FF + "/wepray_business/reading_plan/testament/testament_final_%d.mp3"
	for i := 1; i <= 60; i++ {
		fmt.Println(fmt.Sprintf(str, i))
	}

}
