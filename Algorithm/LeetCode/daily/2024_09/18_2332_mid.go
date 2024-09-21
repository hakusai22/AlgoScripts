package _024_09

import "sort"

// latestTimeCatchTheBus 计算最晚登车时间以抓住巴士。
// 参数:
//
//	buses []int: 巴士发车时间数组。
//	passengers []int: 乘客到达时间数组。
//	capacity int: 巴士容量。
//
// 返回值:
//
//	int: 乘客可以最晚登车的时间。
//
// 说明:
//
//	该函数通过排序巴士和乘客数组，然后模拟每个巴士的乘客搭载过程来找到最晚登车时间。
//	它考虑了巴士容量限制，并在达到巴士时间之前尽可能多的乘客。
//	时间复杂度: O(n log n)，其中 n 是巴士或乘客的数量。
//	空间复杂度: O(1)，使用了额外常数空间。
func latestTimeCatchTheBus(buses []int, passengers []int, capacity int) int {
	// 对巴士和乘客时间进行排序，以便按时间顺序处理。
	sort.Ints(buses)
	sort.Ints(passengers)

	// j 用于追踪当前处理的乘客索引，c 用于记录当前巴士剩余容量。
	j, c := 0, 0

	// 遍历每个巴士的发车时间。
	for _, t := range buses {
		// 重置当前巴士的容量。
		c = capacity

		// 当巴士还有空位，且还有未处理的乘客，且下一个乘客能在当前巴士发车前上车时，让乘客上车。
		for c > 0 && j < len(passengers) && passengers[j] <= t {
			j++
			c--
		}
	}

	// j 减一，因为我们可能在最后一个巴士发车时间之后没有乘客，或者最后一个乘客已经在巴士上。
	j--

	// 初始化答案为最后一个巴士的发车时间，这是理论上最晚可以登车的时间。
	ans := buses[len(buses)-1]

	// 如果最后一个巴士满员了，那么最晚登车时间是最后一个上车乘客的时间。
	if c == 0 {
		ans = passengers[j]
	}

	// 如果最晚登车时间与任何乘客到达时间相同，我们需要回溯到前一个时间，以确保不会与任何乘客冲突。
	for j >= 0 && ans == passengers[j] {
		ans--
		j--
	}

	// 返回最终计算出的最晚登车时间。
	return ans
}
