package main

import (
	"fmt"
	"strings"
	"testing"
)

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/09/13 09:48
    @题目     :
    @参考     :
    @时间复杂度:
    @空间复杂度:

 数据范围:

*/

func TestName(t *testing.T) {
	str := "### Baptism of Jesus (Matthew 3)"
	all := strings.ReplaceAll(str, "###", "")
	fmt.Println(all)
}
