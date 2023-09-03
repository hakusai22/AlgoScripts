/*
 * @Author: hakusai
 * @Date: 2023-05-21 18:04:38
 * @LastEditTime: 2023-05-21 19:19:34
 * @Description:
 */

package _023_05

import (
	"fmt"
	"math"
)

func storeWater(bucket []int, vat []int) int {
	mx := 0
	for _, x := range vat {
		mx = max(mx, x)
	}
	if mx == 0 {
		return 0
	}
	ans := math.MaxInt32
	fmt.Println(ans)
	for x := 1; x <= mx; x++ {
		y := 0
		for i, v := range vat {
			y += max(0, (v+x-1)/x-bucket[i])
		}
		ans = min(ans, x+y)
	}
	return ans
}
