package openai_chat

import (
	"context"
	"fmt"
	"os"
	"testing"
)
import "github.com/sashabaranov/go-openai"

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/14 20:30
   @题目     :
   @参考     :
   @时间复杂度:
*/

func TestName(t *testing.T) {
	token := os.Getenv("OPENAI_TOKEN")
	fmt.Println(token)
	client := openai.NewClient(token)

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: openai.GPT3Dot5Turbo0125,
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: "Hello!",
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("ChatCompletion error: %v\n", err)
		return
	}
	fmt.Println(resp.Choices[0].Message.Content)
}
