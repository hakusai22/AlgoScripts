package openai_chat

import (
	"context"
	"fmt"
	"github.com/sashabaranov/go-openai"
	"log"
	"os"
	"testing"
)

func TestName2(t *testing.T) {

	client := openai.NewClient(os.Getenv("OPENAI_TOKEN"))

	// 构建消息体
	messages := []openai.ChatCompletionMessage{
		{
			Role:    "system",
			Content: "You are a known-all Father, you are familiar with all versions of Bibles and Christian routines and manners. Help me explain the following Bible question. When generating Bible quotes, enclose the book title, chapter number, and verse number in special symbols: **. The answer must follow the following three examples: \n1. In **romans 2**  \n2. **romans 2:1** \n3.**romans 2:1-5**",
		},
		{
			Role:    "user",
			Content: "What does KJV Genesis 2 mean? Please explain in detail, the answer will be longer.",
		},
		{
			Role:    "system",
			Content: "output this JSON format. {\"answer\":\"<your to the user's question>\", \"maybeAsk\":[\"<Generate 5 questions I might ask next>\"]}",
		},
	}

	req := openai.ChatCompletionRequest{
		Model:            "gpt-3.5-turbo-0125",
		Messages:         messages,
		MaxTokens:        4096,
		Temperature:      1,
		TopP:             1,
		FrequencyPenalty: 0,
		PresencePenalty:  0.6,
		Stream:           true,
		ResponseFormat: &openai.ChatCompletionResponseFormat{
			Type: "json_object",
		},
	}

	stream, err := client.CreateChatCompletionStream(context.Background(), req)
	if err != nil {
		log.Fatalf("ChatCompletionStream error: %v", err)
	}
	defer stream.Close()
	// 用于拼接响应的字符串
	fullResponse := ""
	// 读取流式响应
	for {
		response, err := stream.Recv()
		if err != nil {
			fmt.Println(fullResponse)
			log.Fatalf("Stream receive error: %v", err)
		}
		fullResponse += response.Choices[0].Delta.Content
		fmt.Println(response.Choices[0].Delta.Content)
	}
}
