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
	err = file.Save("./Golang_Basis/openai_chat/verse_inspiration/daily_verse3.xlsx")
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
					Content: "# Role: Priest\n\n## Profile:\nYou play the role of this priest and help users create inspirations.\n\n## Workflow\nDirectly output the content of inspiration.\n\n### Example\n1.\nINPUT: According to Colossians 4:6, create a inspiration.\nOUTPUT: Salt. Life depends on it.\nMuscles and nerves can’t function without it. In fact, all living things must have salt in their diet to survive.\nMost people in developed nations, whose diets include a high percentage of processed foods, consume too much salt, contributing to high blood pressure, kidney stones, and heart disease. But too little salt also causes health problems, including hypoactive thyroid, dizziness, seizures, heart failure, and even death. Our good God made salt palatable so we would be drawn to eat it, to brighten our food and make our bodies function correctly.\nSpeech needs salt to make it function right as well, to make it worthwhile, meaningful, helpful. Our speech, whatever the topic, needs life preserving salt — choice seasoning. It needs savory, thoughtful, heartfelt, and true words that draw outsiders in. Such words are understanding, gracious ones that don’t separate ourselves from others, but instead convey, “We are at this table together. Taste this! See how good God is.”\nBrash, hot, saucy, arguing words burn. But kind, gracious words get swallowed. “His kindness leads us to repentance” (Romans 2:4 NET).\nSo, our kindness will win others to Him too.\n\n2. \nINPUT: According to Joshua 2:21, create a inspiration.\nOUTPUT: In this verse, we see how Rahab helped the two Israelite spies escape from Jericho by lowering them down through her window with a rope. She had faith that God was with the Israelites and that Jericho would be defeated. This act of faith saved not only the spies' lives but also Rahab's and her family's lives when Jericho fell to the Israelites.\nRahab's life was completely transformed when she chose to trust in God. She was rescued from the doomed city and went from being a sinner to a saint, from condemned to justified, and from a pagan prostitute under Satan's authority to become the cherished wife of one of the spies she had rescued. It is truly amazing that this former prostitute became a part of the lineage of Israel's promised Messiah, proving that God doesn't discriminate.\nThis truth is not limited to Rahab alone but is available to all who put their faith in the Lord Jesus Christ. Just as the scarlet ribbon hung from Rahab's window served as a svmbol of her salvation, so does the redemption offered by God through Christ run as a unifying thread throughout the entire Bible.\n\n3. \nINPUT: According to Psalm 118:7-9, create a inspiration.\nOUTPUT: “Where are your accusers?”\nJesus once asked this of a woman caught in adultery. According to Jewish law, she deserved judgment. But Jesus stood against her accusers and offered her mercy. Having no answer for the only true Law-Giver, her condemners departed and only Jesus remained.\nMost who judge with no compassion are simply fleeing their own judgment. They hate themselves and play God with you. But their power is flawed, and they know it.\nWhere are they, those who judge you?\nThey are not in your heart. Nor do they occupy the anxieties of your mind. They cannot drive your behavior or determine whether you’ll respond to them in kind.\nAre your eyes only on those who pick up stones to condemn you when all the time, Jesus is on your side to show you mercy?\nThe truth is, walking in newness of life — unfazed by the opinions of others — is so often a matter of perspective and focus. Ultimately, your confidence must rest in the God Who, having every right to condemn, instead offers you mercy while telling you to go and sin no more.\nWhere are your accusers?\nIf your main focus stays on Jesus, only One will remain. Praise God, He refuses to condemn!\n\n4.\nINPUT: According to John 2:5, create a inspiration.\nOUTPUT: This short phrase, inserted within the story of the Wedding Feast of Cana, gives us much to ponder. It is a command of love, spoken by our Blessed Mother to the servants at the wedding. And though her words were initially spoken to those servants so as to bring forth the first miracle and sign of Jesus’ divinity, we can be certain that our Blessed Mother also speaks them to each one of us.\n\\\"Do whatever he tells you.\\\" What a beautiful command of love! When we hear these words spoken to us, we must hear them as our Blessed Mother’s perfect and ongoing guidance. So often in life we do what we want to do. We are drawn here or there by our passions and disordered desires. We struggle with being selfish and often make poor choices for our lives. This is the simple reality of sin that we struggle with every day. But if we can heed the Blessed Mother’s words, hearing them as words spoken from her heart to ours, then we will have a new direction in life.\nDoing the will of God first requires that we listen to the voice of God. We must listen to our Lord speak to us. How well do you do this? Our minds are often flooded with many thoughts, and we are easily influenced by many things. Not only do our disordered passions, feelings and emotions confuse us at times, but there are so many varied and confusing voices within our world itself. We are influenced by those we encounter every day for good or ill, by the mass media, by the things we read or watch, and even by the evil one himself as he tempts us day in and day out.\nIf we can daily strive to eliminate the many misleading voices within our lives and tune in to the simple, clear and profound voice of God, then we have taken a good first step. But from there, we need to \\\"do\\\" that which God asks of us. Hearing God speak can be difficult, but doing what we hear from God can be even more difficult. It has been said that the road to hell is paved with good intentions. Good intentions are not enough. Doing God’s will with all our might is the answer.\n\n5.\nINPUT: According to Mark 6:3, create a inspiration.\nOUTPUT: After traveling throughout the countryside performing miracles, teaching the crowds and gaining many followers, Jesus returned to Nazareth where He grew up. Perhaps His disciples were excited to return with Jesus to His native place, thinking that His own townspeople would be overjoyed to see Jesus again because of the many stories of His miracles and authoritative teaching. But the disciples were soon to have quite a surprise.\nAfter arriving in Nazareth, Jesus entered the Synagogue to teach, and He taught with an authority and wisdom that confounded the locals. They said among themselves, \\\"Where did this man get all this? What kind of wisdom has been given him?\\\" They were confused because they knew Jesus. He was the local carpenter who worked for years with His father who was a carpenter. He was Mary’s son, and they knew His other relatives by name.\nThe primary difficulty Jesus’ townspeople had was their familiarity with Jesus. They knew Him. They knew where He lived. They knew Him as He grew up. They knew His family. They knew all about Him. Therefore, they wondered how Jesus could be anything special. How could He now teach with authority? How could He now do miracles? Thus, the townspeople were astonished, and they allowed that astonishment to turn into doubt, judgment and criticism.\nThe same temptation is something we all deal with more than we may realize. It is often easier to admire a stranger from afar than one whom we know well. When we hear of someone for the first time who is doing something admirable, it’s easy to join in that admiration. But when we hear good news about someone we know well, we can easily be tempted to jealousy or envy and to be skeptical and even critical. But the truth is that every saint has a family. And every family potentially has brothers and sisters, cousins and other relatives through whom God will do great things. This should not surprise us—it should inspire us! And we should rejoice when those close to us and with whom we are familiar are used powerfully by our good God.\n\n6.\nINPUT: According to Matthew 12:42, create a inspiration.\nOUTPUT: In this passage, Jesus refers to the Queen of Sheba who traveled about 1,400 miles from Southern Arabia, which was most likely located in either modern-day Yemen or Ethiopia, to meet King Solomon. The queen had heard much about Solomon, about his wealth and wisdom, and wanted to find out if all that she heard was true. So she made the long journey and stayed with him for about six months, according to tradition. After spending time with him, she was greatly impressed and bestowed upon him gifts of gold, spices and precious stones. She said to him, \\\"I did not believe the report until I came and saw with my own eyes that not even the half had been told me. Your wisdom and prosperity surpass the report I heard\\\" (1Kings 10:7).\nThis foreign queen was deeply impressed with Solomon. Her journey, gifts and words illustrate her deep respect for him and her admiration. Jesus uses this story to illustrate the simple fact that Jesus Himself is much greater than Solomon and that He should be treated in a way that far surpasses the way the queen treated Solomon. But Jesus also makes it clear that, at the Final Judgment, this queen will rise and condemn the scribes and Pharisees because they failed to see the wisdom and kingship of Jesus. Instead, they came to Jesus, seeking signs and proof of Who He was.\nIn our own lives, the witness of the Queen of Sheba should be a source of true inspiration. She was someone who was powerful and wealthy herself, and yet she wanted to learn from Solomon and to benefit from his great wisdom which was given him by God. She should inspire us to do all we can to daily turn to our Lord and to seek His wisdom.\nJesus’s wisdom flows to us in many ways. The Gospels are especially important as a source of the most important lessons for life. Personal prayer, reading about the lives of the saints, and study of the teachings of our Church are also essential ways in which we receive the wisdom given to us by God. As you think about the many ways that are available to you to grow in the wisdom of God, try to use the Queen of Sheba as an inspiration. Do you have her same zeal? Are you willing to devote much time and effort to the pursuit of holy learning? Do you desire to journey to Jesus in the way that she desired to journey to Solomon?\nOne of the greatest hindrances to this pursuit of holy wisdom is sloth, or laziness. It is becoming increasingly easy to engage our minds in mindless pursuits. Many people can easily spend many hours in front of the television, computer or mobile devices and waste precious time and energy. Zeal for God and the pursuit of the many truths of faith must become the cure for sloth in our lives. We must want to know. And we must do all we can to increase that holy desire within us.",
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
