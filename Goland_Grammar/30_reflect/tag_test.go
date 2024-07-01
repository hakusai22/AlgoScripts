package main

import (
	"fmt"
	"reflect"
	"testing"
)

/*
   --idea
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2024/05/05 17:04
*/

type Author struct {
	Name         int      `json:Name`
	Publications []string `json:Publication,omitempty`
}

func TestGetTag(t1 *testing.T) {
	t := reflect.TypeOf(Author{})
	for i := 0; i < t.NumField(); i++ {
		name := t.Field(i).Name
		s, _ := t.FieldByName(name)
		fmt.Println(name, s.Tag)
	}
}
