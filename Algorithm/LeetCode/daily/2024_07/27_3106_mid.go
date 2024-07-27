package _024_07

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/27 22:13
   @题目     :
   @参考     :
   @时间复杂度:
*/

func getSmallestString(s string, k int) string {
	bytes := []byte(s)
	for i, c := range bytes {
		dis := int(min(c-'a', 'z'-c+1))
		if dis > k {
			bytes[i] -= byte(k)
			break
		}
		bytes[i] = 'a'
		k -= dis
	}
	return string(bytes)
}
