package 第285场

import "math"

func maximumBobPoints(numArrows int, aliceArrows []int) []int {
	maxPoint := math.MinInt64
	var ans []int
	backtrack(numArrows, aliceArrows, []int{}, 0, &maxPoint, &ans)
	return ans
}

func backtrack(numArrows int, aliceArrows []int, bob []int, point int, maxPoint *int, ans *[]int) {
	if numArrows >= 0 && len(bob) == len(aliceArrows) {
		if point > *maxPoint {
			bob[0] += numArrows
			*maxPoint = point
			*ans = (*ans)[0:0]
			*ans = append(*ans, bob...)
		}
		return
	}
	if numArrows < 0 || len(bob) >= len(aliceArrows) {
		return
	}
	//得分
	bob = append(bob, aliceArrows[len(bob)]+1)
	backtrack(numArrows-bob[len(bob)-1], aliceArrows, bob, point+len(bob)-1, maxPoint, ans)
	bob = bob[:len(bob)-1]
	//不得分
	bob = append(bob, 0)
	backtrack(numArrows, aliceArrows, bob, point, maxPoint, ans)
	bob = bob[:len(bob)-1]
}
