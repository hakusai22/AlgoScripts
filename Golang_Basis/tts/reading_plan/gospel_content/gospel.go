package main

import (
	"bytes"
	"fmt"
	"github.com/tealeg/xlsx"
	"io"
	"log"
	"net/http"
	"os"
	"strings"
)

func main() {
	//prayer := ""
	file, err := xlsx.OpenFile("./Golang_Basis/tts/reading_plan/gospel_content/gospel2.xlsx")
	if err != nil {
		log.Fatal(err)
	}

	// 读取第一个工作表
	sheet := file.Sheets[0]
	fmt.Println(sheet)
	// 遍历所有行
	for rowIndex, row := range sheet.Rows {
		if rowIndex != 13 { // 跳过标题行
			continue
		}
		introduction_key := row.Cells[0].String()
		introduction_key = strings.TrimSpace(introduction_key)
		introduction_key = strings.ReplaceAll(introduction_key, " ", "_")
		introduction_content := row.Cells[1].String()
		introduction_key = strings.TrimSpace(introduction_key)
		fmt.Println(introduction_key)
		fmt.Println(introduction_content)
		handleTTS(introduction_key, introduction_content)
	}

}

func handleTTS(introduction_key, prayer string) {
	voiceRate := "-10%"
	ssml := fmt.Sprintf(`
    <speak version='1.0' xml:lang='en-US'>
        <voice xml:lang='en-US' xml:gender='Female' name='en-US-AvaMultilingualNeural'>
           	<prosody rate="%s">
             	%s
			<break time="2000ms" />
			</prosody>
        </voice>
    </speak>
    `, voiceRate, prayer)

	tts_key := os.Getenv("TTS_KEY")
	fmt.Println(tts_key)
	// Define the headers
	// "X-Microsoft-OutputFormat":  "audio-24khz-96kbitrate-mono-mp3",
	// "X-Microsoft-OutputFormat":  "riff-24khz-16bit-mono-pcm",
	headers := map[string]string{
		"X-Microsoft-OutputFormat":  "riff-24khz-16bit-mono-pcm",
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

	// Create the output file
	fileName := "./Golang_Basis/tts/reading_plan/gospel_content/mp3_2/" + introduction_key + ".mp3"
	file, err := os.Create(fileName)
	if err != nil {
		log.Fatalf("Error creating file: %v", err)
	}
	defer file.Close()

	// Stream the response body to the file
	_, err = io.Copy(file, resp.Body)
	if err != nil {
		log.Fatalf("Error copying response to file: %v", err)
	}

	fmt.Printf("Audio saved to %s\n", fileName)
}
