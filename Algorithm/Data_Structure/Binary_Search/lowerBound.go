package main

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/08/10 13:37
    @题目     :
    @参考     :
    @时间复杂度:
    @空间复杂度:

 数据范围:

*/

// lowerBound 返回最小的满足 nums[i] >= target 的 i
// 如果数组为空，或者所有数都 < target，则返回 len(nums)
// 要求 nums 是非递减的，即 nums[i] <= nums[i + 1]

// 闭区间写法
func lowerBound(nums []int, target int) int {
	left, right := 0, len(nums)-1 // 闭区间 [left, right]
	for left <= right {           // 区间不为空
		// 循环不变量：
		// nums[left-1] < target
		// nums[right+1] >= target
		mid := left + (right-left)/2
		if nums[mid] < target {
			left = mid + 1 // 范围缩小到 [mid+1, right]
		} else {
			right = mid - 1 // 范围缩小到 [left, mid-1]
		}
	}
	return left
}

// 左闭右开区间写法
func lowerBound2(nums []int, target int) int {
	left, right := 0, len(nums) // 左闭右开区间 [left, right)
	for left < right {          // 区间不为空
		// 循环不变量：
		// nums[left-1] < target
		// nums[right] >= target
		mid := left + (right-left)/2
		if nums[mid] < target {
			left = mid + 1 // 范围缩小到 [mid+1, right)
		} else {
			right = mid // 范围缩小到 [left, mid)
		}
	}
	return left // 返回 left 还是 right 都行，因为循环结束后 left == right
}

// 开区间写法
func lowerBound3(nums []int, target int) int {
	left, right := -1, len(nums) // 开区间 (left, right)
	for left+1 < right {         // 区间不为空
		// 循环不变量：
		// nums[left] < target
		// nums[right] >= target
		mid := left + (right-left)/2
		if nums[mid] < target {
			left = mid // 范围缩小到 (mid, right)
		} else {
			right = mid // 范围缩小到 (left, mid)
		}
	}
	return right
}
