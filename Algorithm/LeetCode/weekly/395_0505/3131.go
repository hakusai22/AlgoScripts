package _95_0505

import "slices"

/*
   --idea
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2024/05/05 00:18
*/

func addedInteger(nums1 []int, nums2 []int) int {
	slices.Sort(nums1)
	slices.Sort(nums2)
	return nums2[0] - nums1[0]
}
