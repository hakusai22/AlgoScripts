package error_test

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/08/04 19:06
*/

import (
	"errors"
	"fmt"
	"testing"
)

type Student struct {
	Name string
}

func TestName(t *testing.T) {
	var stu *Student
	fmt.Println(stu.Name)
}

func TestName2(t *testing.T) {
	defer func() {
		if err := recover(); err != nil {
			fmt.Println("程序发生异常,异常信息:", err)
		}
	}()

	var stu *Student
	fmt.Println(stu.Name)
}

func TestName3(t *testing.T) {
	var stu *Student
	if err := printName(stu); err != nil {
		fmt.Println(err)
	}
}

func printName(stu *Student) error {
	if stu == nil {
		return errors.New("param is nil")
	}
	fmt.Println(stu.Name)
	return nil
}
