package main

import (
	"bytes"
	"fmt"
	"io"
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
	prayer := "First Kings Nineteen:One-Eighteen \n<break time=\"1000ms\" /> And Ahab told Jezebel all that Elijah had done, and withal how he had slain all the prophets with the sword.\nThen Jezebel sent a messenger unto Elijah, saying, So let the gods do to me, and more also, if I make not thy life as the life of one of them by to morrow about this time.\nAnd when he saw that, he arose, and went for his life, and came to Beersheba, which belongeth to Judah, and left his servant there.\nBut he himself went a day's journey into the wilderness, and came and sat down under a juniper tree: and he requested for himself that he might die; and said, It is enough; now, O LORD, take away my life; for I am not better than my fathers.\nAnd as he lay and slept under a juniper tree, behold, then an angel touched him, and said unto him, Arise and eat.\nAnd he looked, and, behold, there was a cake baken on the coals, and a cruse of water at his head. And he did eat and drink, and laid him down again.\nAnd the angel of the LORD came again the second time, and touched him, and said, Arise and eat; because the journey is too great for thee.\nAnd he arose, and did eat and drink, and went in the strength of that meat forty days and forty nights unto Horeb the mount of God.\nAnd he came thither unto a cave, and lodged there; and, behold, the word of the LORD came to him, and he said unto him, What doest thou here, Elijah?\nAnd he said, I have been very jealous for the LORD God of hosts: for the children of Israel have forsaken thy covenant, thrown down thine altars, and slain thy prophets with the sword; and I, even I only, am left; and they seek my life, to take it away.\nAnd he said, Go forth, and stand upon the mount before the LORD. And, behold, the LORD passed by, and a great and strong wind rent the mountains, and brake in pieces the rocks before the LORD; but the LORD was not in the wind: and after the wind an earthquake; but the LORD was not in the earthquake:\nAnd after the earthquake a fire; but the LORD was not in the fire: and after the fire a still small voice.\nAnd it was so, when Elijah heard it, that he wrapped his face in his mantle, and went out, and stood in the entering in of the cave. And, behold, there came a voice unto him, and said, What doest thou here, Elijah?\nAnd he said, I have been very jealous for the LORD God of hosts: because the children of Israel have forsaken thy covenant, thrown down thine altars, and slain thy prophets with the sword; and I, even I only, am left; and they seek my life, to take it away.\nAnd the LORD said unto him, Go, return on thy way to the wilderness of Damascus: and when thou comest, anoint Hazael to be king over Syria:\nAnd Jehu the son of Nimshi shalt thou anoint to be king over Israel: and Elisha the son of Shaphat of Abelmeholah shalt thou anoint to be prophet in thy room.\nAnd it shall come to pass, that him that escapeth the sword of Hazael shall Jehu slay: and him that escapeth from the sword of Jehu shall Elisha slay.\nYet I have left me seven thousand in Israel, all the knees which have not bowed unto Baal, and every mouth which hath not kissed him."
	fmt.Println(len(prayer))
	handleTTS(prayer)
}

func handleTTS(prayer string) {
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
	// "X-Microsoft-OutputFormat":  "riff-24khz-16bit-mono-pcm",
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

	// Create the output file
	fileName := "./Golang_Basis/tts/1_Kings_19_1-18.mp3"
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
