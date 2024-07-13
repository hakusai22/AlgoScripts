package Bit_Operations

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
	"strconv"
	"strings"
)

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/16 12:49
*/

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	a := make([]int, n)
	var line string
	var strs []string
	in.ReadString('\n')
	line, _ = in.ReadString('\n')
	strs = strings.Fields(line)
	for i := 0; i < n; i++ {
		a[i], _ = strconv.Atoi(strs[i])
	}
	res := make([]string, n)
	for i := 0; i < n; i++ {
		res[i] = strconv.Itoa(bits.OnesCount(uint(a[i])))

	}
	fmt.Println(strings.Join(res, " "))
}
