package main

import (
	"context"
	"fmt"
	"github.com/sashabaranov/go-openai"
	"github.com/tealeg/xlsx"
	"log"
	"os"
)

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/14 21:13
   @题目     :
   @参考     :
   @时间复杂度:
*/

func main() {
	// 打开Excel文件
	file, err := xlsx.OpenFile("./Golang_Basis/openai_chat/verse_inspiration/daily_verse2.xlsx")
	if err != nil {
		log.Fatal(err)
	}

	// 读取第一个工作表
	sheet := file.Sheets[0]
	fmt.Println(sheet)
	// 遍历所有行
	for rowIndex, row := range sheet.Rows {
		if rowIndex == 0 { // 跳过标题行
			continue
		}
		// 读取"Chapter and Verse"列，这里假设是第4列（列索引从0开始）
		originalText := row.Cells[1].String()
		fmt.Println(originalText)
		// 调用OpenAI API进行重写
		rewrittenText := rewriteWithOpenAI(originalText)
		fmt.Println(rewrittenText)
		// 将重写后的数据写回到Excel的同一列
		row.Cells[5].Value = rewrittenText
	}

	// 保存修改后的Excel文件
	err = file.Save("./Golang_Basis/openai_chat/verse_inspiration/daily_verse4.xlsx")
	if err != nil {
		log.Fatal(err)
	}
}

func rewriteWithOpenAI(text string) string {
	token := os.Getenv("OPENAI_TOKEN")
	fmt.Println(token)
	client := openai.NewClient(token)
	content := ", Do not bring the original text of the verse."

	resp, _ := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: openai.GPT4o,
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleSystem,
					Content: "# Role: Priest\n\n## Profile:\nWePray is an app for Christian users. One of the functions in WePray app is to talk with AI priests. You play the role of this priest and help users solve problems.\n\n## Constraints\n1. Don't reveal or mention your identity.\n2. When asked about your identity, just reply \\\"I'm just a faith companion.\\\"\n\n## Workflow\n1. Analyze the context and generate the 5 most likely questions the user will ask next.\n2. Output in json format: {\\\"maybeAsk\\\":[\\\"<The 5 questions output from the previous step>\\\"]}.",
				},
				{
					Role:    openai.ChatMessageRoleUser,
					Content: text + content,
				},
			},
		},
	)
	return resp.Choices[0].Message.Content
}
