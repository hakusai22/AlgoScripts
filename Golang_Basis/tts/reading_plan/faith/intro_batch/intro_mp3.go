package main

import (
	"bufio"
	"bytes"
	"fmt"
	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/credentials"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/s3"
	"io/ioutil"
	"log"
	"net/http"
	"os"
)

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/09/10 11:38
    @题目     :
    @参考     :
    @时间复杂度:
    @空间复杂度:

 数据范围:

*/

func main() {
	////prayer := ""
	//file, err := xlsx.OpenFile("./Golang_Basis/tts/reading_plan/faith/intro_batch/faith_intro.xlsx")
	//if err != nil {
	//	log.Fatal(err)
	//}
	//
	//// 读取第一个工作表
	//sheet := file.Sheets[0]
	//fmt.Println(sheet)
	//// 遍历所有行
	//for rowIndex, row := range sheet.Rows {
	//	if rowIndex == 0 { // 跳过标题行
	//		continue
	//	}
	//	introduction_key := row.Cells[0].String()
	//	if introduction_key == "" || len(introduction_key) == 0 {
	//		break
	//	}
	//	introduction_content := row.Cells[1].String()
	//	fmt.Println(introduction_key)
	//	fmt.Println(introduction_content)
	//	handleTTS3(introduction_key, introduction_content)
	//}

	handleTTS3("faith_intro_6", "Can you believe we’re on day six already? Today, we’re diving into the big questions of life, like “Why, God?” In Job 38-42, we get front-row seats to one of the most intense QA sessions in the Bible. Job has been through the wringer, and he’s got plenty of questions for God. But instead of answers, God shows him the vastness of His wisdom. Spoiler alert: Job doesn’t get all the answers, but he walks away with something better—trust. Today’s about trusting God even when we don’t understand. Ready to be humbled in the best way possible? Let’s jump in!")

}

func handleTTS3(introduction_key, introduction_content string) string {
	ssml := fmt.Sprintf(`
    <speak version='1.0' xml:lang='en-US'>
        <voice xml:lang='en-US' xml:gender='Female' name='en-US-AvaMultilingualNeural'>
           %s
			<break time="2000ms" />
        </voice>
    </speak>
    `, introduction_content)

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
	bucketName := os.Getenv("BUCKET_NAME")
	keyName := fmt.Sprintf("wepray_business/reading_plan/faith/%s.mp3", introduction_key)
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
	DOMAIN_FF := os.Getenv("DOMAIN_FF")

	fileURL := fmt.Sprintf("%s/%s", DOMAIN_FF, keyName)
	fmt.Printf("Audio file uploaded successfully. File URL: %s\n", fileURL)
	// 打开文件，如果文件不存在则创建，文件存在则追加内容
	file_txt, err := os.OpenFile("./Golang_Basis/tts/reading_plan/faith/intro_batch/intro_urls.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	// 创建一个新的写入器
	writer := bufio.NewWriter(file_txt)
	writer.WriteString(fileURL + "\n")
	writer.Flush()
	file_txt.Close()
	return fileURL
}
