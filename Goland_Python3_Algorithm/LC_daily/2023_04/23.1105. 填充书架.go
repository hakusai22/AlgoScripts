package _023_04

/*
 * @Author: hakusai
 * @Date: 2023-04-23 21:56:26
 * @LastEditTime: 2023-04-23 22:08:45
 */
func minHeightShelves(books [][]int, shelfWidth int) int {
	n := len(books)
	f := make([]int, n+1)
	for i := 1; i <= n; i++ {
		w, h := books[i-1][0], books[i-1][1]
		f[i] = f[i-1] + h
		for j := i - 1; i > 0; j-- {
			w += books[j-1][0]
			if w > shelfWidth {
				break
			}
			h = max(h, books[j-1][1])
			f[i] = min(f[i], f[j-1]+h)
		}
	}
	return f[n]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
