package 第285场

func countHillValley(nums []int) int {
	var res, n = 0, len(nums)
	for i := 1; i < n-1; i++ {
		l, r := i, i
		for ; l >= 0 && nums[i] == nums[l]; l-- {
		}
		for ; r <= n-1 && nums[i] == nums[r]; r++ {
		}
		if l >= 0 && r <= n-1 {
			if ((nums[i] > nums[l] && nums[i] > nums[r]) ||
				(nums[i] < nums[l] && nums[i] < nums[r])) && nums[i] != nums[i-1] {
				res++
			}
		}
	}
	return res
}
