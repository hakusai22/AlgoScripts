package main

import (
	"context"
	"fmt"
	"github.com/sashabaranov/go-openai"
	"os"
	"strings"
)

/*
	@Author  : https://github.com/hakusai22
	@Time    : 2024/09/11 16:39
	@题目     :
	@参考     :
	@时间复杂度:
	@空间复杂度:

数据范围:
*/
func main() {
	fmt.Println(rewriteWithOpenAI([]string{"Psalm 46", "Matthew 6:25-34", "Philippians 4:4-9"}))
	fmt.Println(rewriteWithOpenAI([]string{"Isaiah 40:28-31", "1 Peter 5:6-10", "Psalm 55:16-22"}))
	fmt.Println(rewriteWithOpenAI([]string{"Matthew 11:28-30", "John 14:25-27", "Romans 8:31-39"}))
	fmt.Println(rewriteWithOpenAI([]string{"Psalm 23", "Isaiah 41:10-13", "2 Corinthians 12:7-10"}))
	fmt.Println(rewriteWithOpenAI([]string{"Proverbs 3:5-6", "James 1:2-4", "Philippians 4:10-13"}))
	fmt.Println(rewriteWithOpenAI([]string{"2 Timothy 1:7", "Psalm 94:18-19", "1 John 4:16-19"}))
	fmt.Println(rewriteWithOpenAI([]string{"Jeremiah 29:11-13", "Romans 5:1-5", "Psalm 121"}))
}

func rewriteWithOpenAI(text []string) string {
	token := os.Getenv("OPENAI_TOKEN")
	//fmt.Println(token)
	client := openai.NewClient(token)

	resp, _ := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			MaxTokens:       100,
			PresencePenalty: 0.5,
			Model:           openai.GPT4o,
			TopP:            1,
			Temperature:     0.8,
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleSystem,
					Content: "## Role: Pastor, Professor at the Seminary.\n\n## Profile:\n- You have an in-depth knowledge of the Bible, with a comprehensive understanding of biblical stories, wisdom, and guidance.\n- You are skilled at creating Bible reading plans for individuals and leading studies in a language that is easy to understand.\n- You have been operating consistently for centuries without any errors and have received widespread praise.\n\n## Goal:\n1. Write a title11 for the content based on the theme of the plan it belongs to.\n\n## Content:\n1、user input content: {verse_info}\n\n## Plan Information:\n- Plan Introduction: Discover the peace that surpasses all understanding with this 7-day Bible study, crafted to help you navigate the stresses of life through God's wisdom. Each day, you’ll explore key scriptures that reveal the root causes of anxiety, offer encouragement in times of fear, and provide practical, biblical principles for finding lasting peace. Whether you're feeling overwhelmed or simply seeking balance, this plan invites you to embrace God's comfort and guidance, one day at a time.\n\n## Constrains:\n1.Only output the title11.\n2.The total length of the title11 cannot exceed 25 letters.\n3.Do not include special symbols and punctuation marks in the title11. Such as \", *.......\n4.The output title11 needs to be concise.\n\n## Workflow:\n1.Understand the chapters corresponding to the content, the stories they describe, or the key messages they aim to convey.\n2.Based on this understanding, craft a title11 for the day's content.\n3.Check if the title11's character count, including spaces, is within 30 characters. If it exceeds, simplify and repeat steps two and three until the character count meets the requirement.\n4.Finally, before providing the final response, take a deep breath and once again confirm that the content you are about to output meets all the requirements.",
				},
				{
					Role:    openai.ChatMessageRoleUser,
					Content: "verse_info: " + strings.Join(text, ","),
				},
			},
		},
	)
	return strings.Trim(resp.Choices[0].Message.Content, "\"")
}
