package _023_09

import (
	"strconv"
	"strings"
)

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/09/04 00:28
*/

type Codec struct {
}

func Constructor() Codec {
	return Codec{}
}

// Serializes a tree to a single string_test.
func (this *Codec) serialize(root *TreeNode) string {
	if root == nil {
		return "null"
	}
	left := this.serialize(root.Left)
	right := this.serialize(root.Right)
	return strconv.Itoa(root.Val) + "," + left + "," + right
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {
	values := strings.Split(data, ",")
	return this.deserializeHelper(&values)
}

func (this *Codec) deserializeHelper(values *[]string) *TreeNode {
	if len(*values) == 0 {
		return nil
	}
	val := (*values)[0]
	*values = (*values)[1:]
	if val == "null" {
		return nil
	}
	intVal, _ := strconv.Atoi(val)
	node := &TreeNode{Val: intVal}
	node.Left = this.deserializeHelper(values)
	node.Right = this.deserializeHelper(values)
	return node
}
