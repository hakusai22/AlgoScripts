package openai_chat

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"github.com/sashabaranov/go-openai"
	"io"
	"io/ioutil"
	"net/http"
	"os"
	"testing"
)

func TestName3(t *testing.T) {

	// 设置API密钥
	apiKey := os.Getenv("OPENAI_TOKEN")

	// 创建请求数据
	requestData := map[string]interface{}{
		"model": "gpt-3.5-turbo-0125",
		"messages": []map[string]string{
			{
				"role":    "system",
				"content": "You are a known-all Father, you are familiar with all versions of Bibles and Christian routines and manners. Help me explain the following Bible question. When generating Bible quotes, enclose the book title, chapter number, and verse number in special symbols: **. The answer must follow the following three examples: \n1. In **romans 2**  \n2. **romans 2:1** \n3.**romans 2:1-5**",
			},
			{
				"role":    "user",
				"content": "What does KJV Genesis 2 mean? Please explain in detail, the answer will be longer.",
			},
			{
				"role":    "system",
				"content": "output this JSON format. {\"answer\":\"<your to the user's question>\", \"maybeAsk\":[\"<Generate 5 questions I might ask next>\"]}",
			},
		},
		"max_tokens":        4096,
		"temperature":       1,
		"top_p":             1,
		"frequency_penalty": 0,
		"presence_penalty":  0.6,
		"response_format": map[string]string{
			"type": "json_object",
		},
	}

	// 序列化请求数据
	jsonData, err := json.Marshal(requestData)
	if err != nil {
		fmt.Println("Error marshaling JSON:", err)
		return
	}

	// 创建HTTP请求
	req, err := http.NewRequest("POST", "https://api.openai.com/v1/chat/completions", bytes.NewBuffer(jsonData))
	if err != nil {
		fmt.Println("Error creating request:", err)
		return
	}

	// 设置请求头
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+apiKey)

	// 发送请求
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println("Error sending request:", err)
		return
	}
	defer resp.Body.Close()

	// 读取响应
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("Error reading response:", err)
		return
	}

	// 输出响应结果
	fmt.Println("Response:", string(body))
}

func TestName4(t *testing.T) {
	// 初始化OpenAI客户端
	apiKey := os.Getenv("OPENAI_TOKEN")
	client := openai.NewClient(apiKey)

	// 构建请求
	req := openai.ChatCompletionRequest{
		Model: "gpt-3.5-turbo-0125",
		Messages: []openai.ChatCompletionMessage{
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
		},
		MaxTokens:        4096,
		Temperature:      1,
		TopP:             1,
		FrequencyPenalty: 0,
		PresencePenalty:  0.6,
		ResponseFormat: &openai.ChatCompletionResponseFormat{
			Type: "json_object",
		},
	}

	// 发送请求
	resp, err := client.CreateChatCompletion(context.Background(), req)
	if err != nil {
		fmt.Println("Error creating chat completion:", err)
		return
	}

	// 输出响应结果
	fmt.Println("Response:", resp.Choices[0].Message.Content)
}

func TestName5(t *testing.T) {
	// 初始化OpenAI客户端
	apiKey := os.Getenv("OPENAI_TOKEN")
	client := openai.NewClient(apiKey)

	// 构建请求
	req := openai.ChatCompletionRequest{
		Model: "gpt-3.5-turbo-0125",
		Messages: []openai.ChatCompletionMessage{
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
		},
		MaxTokens:        4096,
		Temperature:      1,
		TopP:             1,
		FrequencyPenalty: 0,
		PresencePenalty:  0.6,
		ResponseFormat: &openai.ChatCompletionResponseFormat{
			Type: "json_object",
		},
	}

	// 发送请求，接收流式响应
	stream, err := client.CreateChatCompletionStream(context.Background(), req)
	if err != nil {
		t.Fatalf("Error creating chat completion stream: %v", err)
	}
	defer stream.Close()

	// 读取流式响应
	fmt.Println("Stream response:")
	for {
		response, err := stream.Recv()
		if err != nil {
			if err == io.EOF {
				break
			}
			t.Fatalf("Error receiving stream response: %v", err)
		}

		// 输出响应内容
		fmt.Print(response.Choices[0].Delta.Content)
	}
}
