package _09_map

import (
	"fmt"
	"testing"
)

/*
--idea
-*- coding: utf-8 -*-
@Author  : hakusai22
@Time    : 2024/05/05 17:07
*/
type Set map[string]struct{}

func TestSet(t *testing.T) {
	set := make(Set)

	for _, item := range []string{"A", "A", "B", "C"} {
		set[item] = struct{}{}
	}
	fmt.Println(len(set)) // 3
	if _, ok := set["A"]; ok {
		fmt.Println("A exists") // A exists
	}
}
