package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/16 13:14
*/

func main() {
	var reader = bufio.NewReader(os.Stdin)
	var xx = readArray(reader, " ")
	var mp = make(map[int]int)
	n, m := xx[0], xx[1]
	for i := 0; i < n; i++ {
		var aa = readArray(reader, " ")
		index, value := aa[0], aa[1]
		mp[index] += value
	}

	var s = make([][]int, n)
	for i := 0; i < m; i++ {
		var bb = readArray(reader, " ")
		if _, ok := mp[bb[0]]; !ok {
			mp[bb[0]] = 0
		}
		if _, ok := mp[bb[1]]; !ok {
			mp[bb[1]] = 0
		}
		s[i] = bb
	}
	var nums []int
	for k := range mp {
		nums = append(nums, k)
	}
	sort.Ints(nums)
	// 生成映射关系
	var p = make(map[int]int)
	for i, k := range nums {
		p[k] = i
	}

	// 计算前缀和
	var sums = make([]int, len(nums)+1)
	for i := 0; i < len(nums); i++ {
		sums[i+1] = sums[i] + mp[nums[i]]
	}

	// 查询
	for i := 0; i < m; i++ {
		fmt.Println(sums[p[s[i][1]]+1] - sums[p[s[i][0]]])
	}
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
