package _1_nil

import (
	"fmt"
	"testing"
)

/*
   --idea
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2024/05/05 17:14
*/

func TestName(t *testing.T) {
	var p *int = nil
	var i interface{} = nil
	if p == i {
		fmt.Println("Equal")
	} else {
		fmt.Println("false")
	}
	var a *int = nil
	var b *int = nil
	fmt.Println(a == b)
}

func TestName2(t *testing.T) {
	var a uint = 1
	var b uint = 2
	fmt.Println(a - b)
}

type Header struct {
}

func TestName3(t *testing.T) {

}
