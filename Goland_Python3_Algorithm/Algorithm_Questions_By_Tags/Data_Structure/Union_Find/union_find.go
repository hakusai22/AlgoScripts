package Union_Find

/*
	并查集
	只有路径压缩的并查集复杂度是 O(nlogn) 的，这也是大多数情况下的实现方案
	只有启发式合并（按深度合并）的并查集的复杂度也是 O(nlogn) 的，适用于可持久化的场景
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/09 23:27
*/

type UnionFind struct {
	Fa     []int
	Groups int // 连通分量个数
}

func NewUnionFind(n int) UnionFind {
	fa := make([]int, n) // n+1
	for i := range fa {
		fa[i] = i
	}
	return UnionFind{fa, n}
}

func (u UnionFind) Find(x int) int {
	if u.Fa[x] != x {
		u.Fa[x] = u.Find(u.Fa[x])
	}
	return u.Fa[x]
}

// newRoot = -1 表示未发生合并
func (u *UnionFind) Merge(from, to int) (newRoot int) {
	x, y := u.Find(from), u.Find(to)
	if x == y {
		return -1
	}
	u.Fa[x] = y
	u.Groups--
	return y
}

func (u UnionFind) Same(x, y int) bool {
	return u.Find(x) == u.Find(y)
}

// 二维并查集
type ufPoint struct{ x, y int } // int32
type uf2d map[ufPoint]ufPoint

func (u uf2d) find(x ufPoint) ufPoint {
	if f, ok := u[x]; ok && f != x {
		u[x] = u.find(f)
		return u[x]
	}
	return x
}
func (u uf2d) merge(from, to ufPoint) { u[u.find(from)] = u.find(to) }
