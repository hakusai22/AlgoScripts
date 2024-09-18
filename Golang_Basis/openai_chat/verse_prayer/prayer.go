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
	file, err := xlsx.OpenFile("./Golang_Basis/openai_chat/verse_prayer/daily_verse2.xlsx")
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
		row.Cells[4].Value = rewrittenText
	}

	// 保存修改后的Excel文件
	err = file.Save("./Golang_Basis/openai_chat/verse_prayer/daily_verse3.xlsx")
	if err != nil {
		log.Fatal(err)
	}
}

func rewriteWithOpenAI(text string) string {
	token := os.Getenv("OPENAI_TOKEN")
	fmt.Println(token)
	client := openai.NewClient(token)

	resp, _ := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: openai.GPT3Dot5Turbo0125,
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleSystem,
					Content: "# Role: Priest\n\n## Profile:\nYou play the role of this priest and help users create prayers.\n\n## Workflow\nDirectly output the content of prayer.\n\n### Example\n1.\nINPUT: According to Isaiah 41:10, create a prayer.\nOUTPUT: Dear Father in heaven, we thank you that you are our Father and that we may have you with us. We thank you that we can know you are leading us by your hand. Give us your Spirit of understanding so that we may always see your mighty and powerful hand guiding us on all our ways. Help us where we fall short. Help us, for we are weak and are often in situations where we cannot help ourselves. But you are strong. You give light to our hearts. Through the Savior, Jesus Christ, we can direct our lives cheerfully, joyfully, and patiently toward the great goal set before us your children, and before the whole world. Amen.\n\n2. \nINPUT: According to Psalm 31:7, create a prayer.\nOUTPUT: Dear Father in heaven, we come before your presence with thanksgiving and rejoice that you are with us on earth. Even though we have many struggles and temptations and even though problems crowd in upon us, we know that we are in your hands and that everything must go according to your will. Hold us securely in your hand. Help us to bear all that we find hard, for we know you are in control and you lead everything to a good end_batch. The darker and more difficult it may seem, the more clearly your hand will reveal the victory in those whose lives are founded in eternity, whose lives cannot end_batch in sorrow but will end_batch in your glory. Amen.\n\n3. \nINPUT: According to 1 John 4:16, create a prayer.\nOUTPUT: Lord our God, we come to you as poor, heavily burdened people who often do not know where to turn. But we have trust in you, for you are love. Your love penetrates deep into our lives, righting what is wrong and making amends for our blundering. And so we are joyful and await your grace and your help on all our ways. Bless us, and help us find what is right in every situation, to your praise and your honor. Amen.\n\n4. \nINPUT: According to John 2:5, create a prayer.\nOUTPUT: Dearest Mother, please speak these words to me every day. As you do, please pray for me that I may listen to all that your Son asks of me and obey His voice with my whole heart. Thank you for your perfect \\\"Yes\\\" and your obedience to God in all things. May I learn to more fully imitate you every day. Mother Mary, pray for us. Jesus, I trust in You.\n\n5. \nINPUT: According to Mark 6:3, create a prayer.\nOUTPUT: My ever-present Lord, thank You for the countless ways in which You are present in the lives of those all around me. Give me the grace to see You and to love You in the lives of those closest to me. As I discover Your glorious presence in their lives, fill me with deep gratitude and help me to acknowledge Your love that comes forth from their lives. Jesus, I trust in You.\n\n6. \nINPUT: According to Matthew 12:42, create a prayer.\nOUTPUT: My Lord of all Wisdom, You are infinitely greater than the wisest of kings and more glorious than anything I can imagine. Please fill me with zeal, dear Lord, so that I will fervently pursue You and daily journey to You. Please guide my prayer and my study so that Your wisdom and Your very Self will be bestowed upon me. Jesus, I trust in You.",
				},
				{
					Role:    openai.ChatMessageRoleUser,
					Content: text,
				},
			},
		},
	)
	return resp.Choices[0].Message.Content
}
