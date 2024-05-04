package _95_0505

import "slices"

/*
--idea
-*- coding: utf-8 -*-
@Author  : hakusai22
@Time    : 2024/05/05 00:26
*/
func minimumAddedInteger(nums1 []int, nums2 []int) int {
	slices.Sort(nums1)
	slices.Sort(nums2)
	for i := 2; i > 0; i-- {
		diff := nums2[0] - nums1[i]
		j := 0
		for _, v := range nums1[i:] {
			if nums2[j] == v+diff {
				j++
				if j == len(nums2) {
					return diff
				}
			}
		}
	}
	return nums2[0] - nums1[0]
}
