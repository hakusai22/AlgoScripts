package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	// 设置TXT文件路径
	filePath := "./Golang_Basis/openai_chat/session_excel/session.txt"

	// 打开TXT文件
	file, err := os.Open(filePath)
	if err != nil {
		log.Fatalf("无法打开TXT文件: %v", err)
	}

	// 读取文件内容
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		originalText := scanner.Text()
		// 进行数据转换
		transformedText := transformData(originalText)
		fmt.Println(transformedText)
	}

	if err := scanner.Err(); err != nil {
		log.Fatalf("读取文件内容时出错: %v", err)
	}
}

// 数据转换函数
func transformData(input string) string {
	// 提取书名和章节
	parts := strings.Split(input, ":")
	if len(parts) < 2 {
		return ""
	}
	bookAndChapter := strings.TrimSpace(parts[1])
	if strings.Contains(input, "Samuel") {
		bookParts := strings.Split(bookAndChapter, " ")
		if len(bookParts) < 2 {
			return ""
		}
		bookName := bookParts[1]
		chapter := strings.Split(bookParts[2], "-")[0]
		// 构造新的字符串
		return fmt.Sprintf("%s_%s", bookName, chapter)
	} else {
		bookParts := strings.Split(bookAndChapter, " ")
		if len(bookParts) < 2 {
			return ""
		}
		bookName := bookParts[0]
		chapter := strings.Split(bookParts[1], "-")[0]

		// 构造新的字符串
		return fmt.Sprintf("%s_%s", bookName, chapter)
	}

}
