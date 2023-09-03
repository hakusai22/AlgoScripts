/*
 * @Author: hakusai
 * @Date: 2023-05-14 23:05:07
 * @LastEditTime: 2023-05-14 23:19:49
 */

package _023_05

import (
	"fmt"
	"sort"
)

func rearrangeBarcodes(barcodes []int) []int {
	mx := 0
	for _, v := range barcodes {
		mx = max(mx, v)
	}
	cnt := make([]int, mx+1)
	for _, v := range barcodes {
		cnt[v]++
	}
	sort.Slice(barcodes, func(i, j int) bool {
		a, b := barcodes[i], barcodes[j]
		if cnt[a] == cnt[b] {
			return a < b
		}
		return cnt[a] > cnt[b]
	})
	n := len(barcodes)
	ans := make([]int, n)
	for k, j := 0, 0; k < 2; k++ {
		for i := k; i < n; i, j = i+2, j+1 {
			ans[i] = barcodes[j]
		}

	}
	return ans
}

func main() {
	fmt.Println("qwerqwer")
}
