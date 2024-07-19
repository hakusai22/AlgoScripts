package main

import (
	"bufio"
	"bytes"
	"fmt"
	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/credentials"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/s3"
	"github.com/tealeg/xlsx"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"strconv"
)

/*
   @Author  : https://github.com/hakusai22
   @Time    : 2024/07/14 21:13
   @题目     :
   @参考     :
   @时间复杂度:
*/

func main() {
	//// 打开Excel文件
	file, err := xlsx.OpenFile("./Golang_Basis/openai_chat/verse_prayer/daily_verse_tts.xlsx")
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
		monthdaycode := row.Cells[0].String()
		prayer := row.Cells[6].String()
		atoi, _ := strconv.Atoi(monthdaycode)
		if atoi <= 220 || atoi >= 708 {
			continue
		}
		fmt.Println(monthdaycode)
		handleTTS_AWS(monthdaycode, prayer)
	}
}

func handleTTS_AWS(monthdaycode string, prayer string) {
	voiceRate := "-20%"
	ssml := fmt.Sprintf(`
    <speak version='1.0' xml:lang='en-US'>
        <voice xml:lang='en-US' xml:gender='Male' name='en-US-BrianMultilingualNeural'>
			 <prosody rate="%s">
             	%s
			</prosody>
        </voice>
    </speak>
    `, voiceRate, prayer)

	tts_key := os.Getenv("TTS_KEY")
	fmt.Println(tts_key)
	// Define the headers
	headers := map[string]string{
		"X-Microsoft-OutputFormat":  "audio-24khz-96kbitrate-mono-mp3",
		"Content-Type":              "application/ssml+xml",
		"Ocp-Apim-Subscription-Key": tts_key,
	}

	url := "https://westus.tts.speech.microsoft.com/cognitiveservices/v1"
	req, err := http.NewRequest("POST", url, bytes.NewBuffer([]byte(ssml)))
	if err != nil {
		log.Fatalf("Error creating request: %v", err)
	}
	for key, value := range headers {
		req.Header.Set(key, value)
	}

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		log.Fatalf("Error making request: %v", err)
	}
	defer resp.Body.Close()

	audioData, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalf("Error reading response body: %v", err)
	}

	// Define AWS S3 credentials
	bucketName := "xxxx"
	keyName := fmt.Sprintf("wepray_business/daily_verse/%s.mp3", monthdaycode)
	accessKeyID := os.Getenv("ACCESS_KEY_ID")
	secretAccessKey := os.Getenv("SECRET_KEY")
	regionName := "us-west-1"

	// Create an S3 client
	sess, err := session.NewSession(&aws.Config{
		Region:      aws.String(regionName),
		Credentials: credentials.NewStaticCredentials(accessKeyID, secretAccessKey, ""),
	})
	if err != nil {
		log.Fatalf("Error creating AWS session: %v", err)
	}
	s3Client := s3.New(sess)

	// Upload the audio data to S3
	_, err = s3Client.PutObject(&s3.PutObjectInput{
		Bucket:      aws.String(bucketName),
		Key:         aws.String(keyName),
		Body:        bytes.NewReader(audioData),
		ContentType: aws.String("audio/mpeg"),
	})
	if err != nil {
		log.Fatalf("Error uploading to S3: %v", err)
	}

	fileURL := fmt.Sprintf("xxxx/%s", keyName)
	fmt.Printf("Audio file uploaded successfully. File URL: %s\n", fileURL)

	// 打开文件，如果文件不存在则创建，文件存在则追加内容
	file_txt, err := os.OpenFile("./urls.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	// 创建一个新的写入器
	writer := bufio.NewWriter(file_txt)
	writer.WriteString(fileURL + "\n")
	writer.Flush()
	file_txt.Close()
}
