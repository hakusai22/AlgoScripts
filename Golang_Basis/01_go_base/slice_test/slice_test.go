package slice_test

import "fmt"

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/13 19:33
   @题目     :
   @参考     :
   @时间复杂度:
*/

// Golang 是值传递
import (
	"testing"
)

func fnA() {
	dat0 := make([]int, 6, 10)
	fmt.Println(dat0)
	handleA(dat0)
	fmt.Println(dat0)
	handleB(&dat0)
	fmt.Println(dat0)
}

func handleA(a []int) {
	a[0] = 200
	fmt.Println(a)
	a = append(a, 120)
	fmt.Println(a)
}

func handleB(a *[]int) {
	*a = append(*a, 120)
	fmt.Println(a)
}

func TestSlice(t *testing.T) {
	fnA()
}
