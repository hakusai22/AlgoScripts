package Prefix_Suffix

import (
	"bufio"
	"fmt"
	"os"
)

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/14 23:05
*/

const N = 1e5 + 10

var n, m int
var a [N]int

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer func(out *bufio.Writer) {
		err := out.Flush()
		if err != nil {

		}
	}(out)
	_, err := fmt.Fscan(in, &n, &m)
	if err != nil {
		return
	}
	for i := 1; i <= n; i++ {
		_, err := fmt.Fscan(in, &a[i])
		if err != nil {
			return
		}
	}
	for i := 1; i <= n; i++ {
		a[i] += a[i-1]
	}
	for i := 0; i < m; i++ {
		var l, r int
		_, err := fmt.Fscan(in, &l, &r)
		if err != nil {
			return
		}
		_, err = fmt.Fprintln(out, a[r]-a[l-1])
		if err != nil {
			return
		}
	}
}
