package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"regexp"
	"strconv"
	"strings"
)

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/09/05 11:12
    @题目     :
    @参考     :
    @时间复杂度:
    @空间复杂度:

 数据范围:

*/

func main() {
	// 调用函数提取指定范围内的段落内容
	chapter := "1-Genesis"
	fileName := "1"
	startNumber := 1
	endNumber := 1

	verseContent, err := getVerseContent(chapter, fileName, startNumber, endNumber)
	if err != nil {
		fmt.Println("错误:", err)
		os.Exit(1)
	}

	fmt.Println("提取指定范围内的段落内容:")
	fmt.Println(verseContent)
}

// getVerseContent 从指定文件中提取指定范围内的段落内容
func getVerseContent(chapter, fileName string, startNumber, endNumber int) (string, error) {
	// 构建文件路径
	filePath := fmt.Sprintf("Golang_Basis/openai_chat/bible/KJV/%s/%s.txt", chapter, fileName)

	// 读取文件内容
	content, err := ioutil.ReadFile(filePath)
	if err != nil {
		return "", fmt.Errorf("无法读取文件: %v", err)
	}

	// 将内容转换为字符串
	text := string(content)

	// 正则表达式提取标签内的数值和内容，处理标签之间的文本
	re := regexp.MustCompile(`<bmstyle[^>]*?>(\d+)</bmstyle>([^<]*)`)
	matches := re.FindAllStringSubmatch(text, -1)

	result := ""

	// 遍历所有匹配的段落
	for _, match := range matches {
		if len(match) > 2 {
			// 提取段落编号
			number, err := strconv.Atoi(match[1])
			if err != nil {
				return "", fmt.Errorf("解析段落编号出错: %v", err)
			}

			// 过滤指定范围的段落
			if number >= startNumber && number <= endNumber {
				// 去除内容中可能的换行和多余空格
				content := strings.TrimSpace(match[2])
				// 将内容添加到结果中
				fmt.Printf("段落 %d: %s\n", number, content)
				result += content
				result += "\n"
			}
		} else {
			fmt.Printf("匹配结果不符合预期: %v\n", match)
		}
	}

	return result, nil
}
