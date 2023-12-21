package Hash_Table

import (
	"sort"
	"strings"
)

/*
--idea
-*- coding: utf-8 -*-
@Author  : hakusai22
@Time    : 2023/12/21 20:59
*/
func groupAnagrams(strs []string) (ans [][]string) {
	mp := make(map[string][]string)
	for _, s := range strs {
		split := strings.Split(s, "")
		sort.Strings(split)
		str := strings.Join(split, "")
		if _, ok := mp[str]; !ok {
			mp[str] = []string{}
		}
		mp[str] = append(mp[str], s)
	}
	for _, val := range mp {
		ans = append(ans, val)
	}
	return
}
