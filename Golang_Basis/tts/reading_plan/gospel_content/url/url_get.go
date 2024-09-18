package main

import (
	"fmt"
	"github.com/tealeg/xlsx"
	"log"
	"os"
	"strings"
)

func main() {
	//prayer := ""
	file, err := xlsx.OpenFile("./Golang_Basis/tts/reading_plan/gospel_content/new.xlsx")
	if err != nil {
		log.Fatal(err)
	}

	// 读取第一个工作表
	sheet := file.Sheets[0]
	fmt.Println(sheet)
	DOMAIN_FF := os.Getenv("DOMAIN_FF")

	str := DOMAIN_FF + "/wepray_business/reading_plan/kjv/"

	for rowIndex, row := range sheet.Rows {
		if rowIndex <= 0 { // 跳过标题行
			continue
		}
		introduction_key := row.Cells[0].String()
		introduction_key = strings.TrimSpace(introduction_key)
		introduction_key = strings.ReplaceAll(introduction_key, " ", "_")
		if introduction_key == "" || len(introduction_key) == 0 {
			break
		}
		fmt.Println(str + introduction_key + ".mp3")
	}

}
