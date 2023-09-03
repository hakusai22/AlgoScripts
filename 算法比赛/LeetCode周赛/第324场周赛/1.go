package main

import "fmt"

func similarPairs(words []string) (ans int) {
	cnt := map[int]int{}
	for _, s := range words {
		mask := 0
		for _, c := range s {
			mask |= 1 << (c - 'a')
		}
		ans += cnt[mask]
		cnt[mask]++
	}
	return
}

func main() {
	var word = []string{"aaa", "a", "aab"}
	fmt.Println(similarPairs(word))
	fmt.Println(111)
}
