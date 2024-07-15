package _2_process_control

import (
	"fmt"
	"testing"
)

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/16 02:12
   @题目     :
   @参考     :
   @时间复杂度:
*/

func TestRange(t *testing.T) {
	s := "abc"
	// 忽略 2nd value，支持 string_test/array/slice/map。
	for i := range s {
		println(s[i])
	}
	// 忽略 index。
	for _, c := range s {
		println(c)
	}
	// 忽略全部返回值，仅迭代。
	for range s {

	}

	m := map[string]int{"a": 1, "b": 2}
	// 返回 (key, value)。
	for k, v := range m {
		println(k, v)
	}

	a := [3]int{0, 1, 2}
	for i, v := range a { // index、value 都是从复制品中取出。
		if i == 0 { // 在修改前，我们先修改原数组。
			a[1], a[2] = 999, 999
			fmt.Println(a) // 确认修改有效，输出 [0, 999, 999]。
		}
		a[i] = v + 100 // 使用复制品中取出的 value 修改原数组。
	}
	fmt.Println(a) // 输出 [100, 101, 102]。

	s11 := []int{1, 2, 3, 4, 5}

	for i, v := range s11 { // 复制 struct slice { pointer, len, cap }。

		if i == 0 {
			s11 = s11[:3] // 对 slice 的修改，不会影响 range。
			s11[2] = 100  // 对底层数据的修改。
		}
		println(i, v)
	}
}
