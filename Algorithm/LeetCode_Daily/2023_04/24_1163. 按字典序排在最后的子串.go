/*
 * @Author: hakusai
 * @Date: 2023-04-24 10:03:30
 * @LastEditTime: 2023-04-24 10:03:41
 */
package _023_04

import (
	"index/suffixarray"
	"unsafe"
)

func lastSubstring(s string) string {
	sa := (*struct {
		_  []byte
		sa []int32
	})(unsafe.Pointer(suffixarray.New([]byte(s)))).sa
	return s[sa[len(s)-1]:]
}
