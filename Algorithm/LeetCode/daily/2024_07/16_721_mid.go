package _024_07

import "slices"

/*
@Author  : https://github.com/hakusai22
@Time    : 2024/07/15 10:53
@题目     :
@参考     :
@时间复杂度:
*/
func accountsMerge(accounts [][]string) [][]string {
	emailToIdx := map[string][]int{}
	for i, account := range accounts {
		for _, email := range account[1:] {
			emailToIdx[email] = append(emailToIdx[email], i)
		}
	}

	vis := make([]bool, len(accounts))
	emailSet := map[string]struct{}{}
	var dfs func(int)
	dfs = func(i int) {
		vis[i] = true
		for _, email := range accounts[i][1:] {
			if _, has := emailSet[email]; has {
				continue
			}
			emailSet[email] = struct{}{}
			for _, j := range emailToIdx[email] {
				if !vis[j] {
					dfs(j)
				}
			}
		}
	}
	var ans [][]string
	for i, b := range vis {
		if b {
			continue
		}
		clear(emailSet)
		dfs(i)
		res := make([]string, 1, len(emailSet)+1)
		res[0] = accounts[i][0]
		for email := range emailSet {
			res = append(res, email)
		}
		slices.Sort(res[1:])
		ans = append(ans, res)
	}
	return ans
}
