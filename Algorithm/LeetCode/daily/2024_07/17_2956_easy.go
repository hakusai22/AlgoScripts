package _024_07

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/16 22:58
   @题目     : https://leetcode.cn/problems/find-common-elements-between-two-arrays/description/?envType=daily-question&envId=2024-07-16
   @参考     : https://leetcode.cn/problems/find-common-elements-between-two-arrays/solutions/2560724/xian-xing-zuo-fa-pythonjavacgo-by-endles-e04u/?envType=daily-question&envId=2024-07-16
   @时间复杂度: 时间复杂度：O(n+m)，其中 n 为 nums
*/

func findIntersectionValues(nums1 []int, nums2 []int) []int {
	set1 := map[int]int{}
	for _, x := range nums1 {
		set1[x] = 1
	}
	set2 := map[int]int{}
	for _, x := range nums2 {
		set2[x] = 1
	}

	ans := [2]int{}
	for _, x := range nums1 {
		ans[0] += set2[x]
	}

	for _, x := range nums2 {
		ans[1] += set1[x]
	}
	return ans[:]
}
