package _69_1126_3

/*
   --idea
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/11/26 17:01
*/
func minSum(nums1, nums2 []int) int64 {
	s1 := int64(0)
	zero1 := false
	for _, x := range nums1 {
		if x == 0 {
			zero1 = true
			s1++
		} else {
			s1 += int64(x)
		}
	}

	s2 := int64(0)
	zero2 := false
	for _, x := range nums2 {
		if x == 0 {
			zero2 = true
			s2++
		} else {
			s2 += int64(x)
		}
	}

	if !zero1 && s1 < s2 || !zero2 && s2 < s1 {
		return -1
	}
	return max(s1, s2)
}

func max(s1 int64, s2 int64) int64 {
	if s1 < s2 {
		return s2
	} else {
		return s1
	}
}
