package main

import (
	"fmt"
	"strings"
)

// strings主要针对utf-8 编码，实现一些简单函数。
func main() {
	//1是否包含指定内容 返回bool类型
	s1 := "ok let's go"
	fmt.Println(strings.Contains(s1, "go"))
	//结果为true

	//是否包含指定的字符串中任意一个字符 有一个出现过 就返回true
	fmt.Println(strings.ContainsAny(s1, "glass"))

	//返回指定字符出现的次数
	fmt.Println(strings.Count(s1, "g"))

	//文本的开头
	fmt.Println(strings.HasPrefix(s1, "ok"))
	//文本的结尾
	fmt.Println(strings.HasSuffix(s1, ".txt"))

	//查找指定字符在字符串中存在的位置 如果不存在返回-1
	fmt.Println(strings.Index(s1, "g"))
	//查找字符中任意一个字符出现在字符串中的位置
	fmt.Println(strings.IndexAny(s1, "s"))
	//查找指定字符出现在字符串中最后一个的位置
	fmt.Println(strings.LastIndex(s1, "s"))

	//字符串的拼接
	s2 := []string{"123n", "abc", "ss"}
	s3 := strings.Join(s2, "_")
	fmt.Println(s3) // 123n_abc_ss

	//字符串的切割
	s4 := strings.Split(s3, "_")
	fmt.Println(s4) // 返回切片[]07_string{"123n","abc","ss"}

	//字符串的替换
	s5 := "okoletsgo"
	s6 := strings.Replace(s5, "o", "*", 1)
	fmt.Println(s6) //*koletsgo
	//TODO 1 只替换1次,  -1 全部替换

	//字符串的截取
	//str[start:end]包含start 不包含end
}
