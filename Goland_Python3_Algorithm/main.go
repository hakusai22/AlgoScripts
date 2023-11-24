package Goland_Python3_Algorithm

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/16 12:35
*/

func main() {
	sc := bufio.NewScanner(os.Stdin)
	bs := make([]byte, 2000*1024)
	sc.Buffer(bs, len(bs))
	sc.Scan()
	N, _ := strconv.Atoi(sc.Text())

	repo := make(map[int]int, N)
	sc.Scan()
	l := strings.Split(sc.Text(), " ")
	for _, s := range l {
		v, _ := strconv.Atoi(s)
		repo[v]++
	}
	sc.Scan()
	M, _ := strconv.Atoi(sc.Text())
	movie := make([][3]int, M)
	sc.Scan()
	l = strings.Split(sc.Text(), " ")
	for i, s := range l {
		movie[i][0], _ = strconv.Atoi(s)
		movie[i][2] = i + 1
	}
	sc.Scan()
	l = strings.Split(sc.Text(), " ")
	for i, s := range l {
		movie[i][1], _ = strconv.Atoi(s)
	}
	sort.Slice(movie, func(i, j int) bool {
		if repo[movie[i][0]] == repo[movie[j][0]] {
			return repo[movie[i][1]] > repo[movie[j][1]]
		} else {
			return repo[movie[i][0]] > repo[movie[j][0]]
		}
	})
	fmt.Println(movie[0][2])
}
