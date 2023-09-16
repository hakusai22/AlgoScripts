package _023_09

import (
	"bufio"
	"strconv"
	"strings"
)

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/04 00:29
*/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func readLine(reader *bufio.Reader) string {
	var line, _ = reader.ReadString('\n')
	return strings.TrimRight(line, "\n")
}

func readArray(reader *bufio.Reader, sep string) []int {
	var line = readLine(reader)
	var strList = strings.Split(line, sep)
	var nums = make([]int, 0)
	var err error
	var v int
	for i := 0; i < len(strList); i++ {
		if v, err = strconv.Atoi(strList[i]); err != nil {
			panic("xxxx")
		}
		nums = append(nums, v)
	}
	return nums
}
