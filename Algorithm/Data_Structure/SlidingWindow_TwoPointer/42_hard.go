package SlidingWindow_TwoPointer

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/08/04 15:34
   @题目     : https://leetcode.cn/problems/trapping-rain-water/
   @参考     :
   @时间复杂度: O(n)，其中 n 为 height 的长度。
   @空间复杂度: O(1)，仅用到若干额外变量。

提示：
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
*/

func trap(height []int) int {
	left, right, preMax, sufMax := 0, len(height)-1, 0, 0
	ans := 0
	for left < right {
		preMax = max(preMax, height[left])
		sufMax = max(sufMax, height[right])
		if preMax < sufMax {
			ans += preMax - height[left]
			left++
		} else {
			ans += sufMax - height[right]
			right--
		}
	}
	return ans
}

func trap2(height []int) (ans int) {
	n := len(height)
	preMax := make([]int, n) // preMax[i] 表示从 height[0] 到 height[i] 的最大值
	preMax[0] = height[0]
	for i := 1; i < n; i++ {
		preMax[i] = max(preMax[i-1], height[i])
	}

	sufMax := make([]int, n) // sufMax[i] 表示从 height[i] 到 height[n-1] 的最大值
	sufMax[n-1] = height[n-1]
	for i := n - 2; i >= 0; i-- {
		sufMax[i] = max(sufMax[i+1], height[i])
	}

	for i, h := range height {
		ans += min(preMax[i], sufMax[i]) - h // 累加每个水桶能接多少水
	}
	return
}
