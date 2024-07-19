package search_engine_demo

import (
	"bufio"
	"fmt"
	"github.com/go-ego/gse"
	"math"
	"os"
	"sort"
	"strings"
	"testing"
)

var globalGse gse.Segmenter

var StopWord = []string{",", ".", "，", "、", "。", "*", "(", ")", "'", "\"", "/", "?"}

type InvertedIndex map[string][]int

func TestSe2(t *testing.T) {
	// 0. 使用gse分词器
	InitConfig()
	query := "歌曲电影"
	cutSearch := globalGse.CutSearch(query)
	fmt.Println(cutSearch)
	// 1. 数据准备
	docx := fileOpen()
	// 2. 构建倒排索引
	iIndex := BuildIndex(docx)
	// 3. 关键字分词进行搜索
	res, qy := search(iIndex, query, docx)
	fmt.Println(res)
	fmt.Println(qy)
	// 4. 对结果使用排名算法TF-IDF进行排序
	resT := sortRes(qy, res)
	fmt.Printf("一共搜索到 %d 条,query 分词结果: %v \n", len(res), qy)
	for i := range resT {
		fmt.Println(resT[i].Score, resT[i].Docx)
	}
}

func InitConfig() {
	globalGse, _ = gse.New()
}

// 读取文件，返回docx 字符串数组
func fileOpen() []string {
	file, err := os.Open("./data/movies.csv")
	if err != nil {
		fmt.Println(err)
	}
	defer func(file *os.File) {
		err := file.Close()
		if err != nil {

		}
	}(file)
	// 创建一个scanner 用来读取文件内容
	scanner := bufio.NewScanner(file)
	docxs := make([]string, 0)
	for scanner.Scan() {
		line := scanner.Text()
		tmp := strings.Split(line, ",")
		docxs = append(docxs, tmp[1])
	}
	docxs = docxs[1:]
	return docxs
}

// removeShopWord 去除一些语气词， 不重要的标点符号
func removeShopWord(word string) string {
	for i := range StopWord {
		word = strings.Replace(word, StopWord[i], "", -1)
	}
	return word
}

// 建立索引
func BuildIndex(docx []string) InvertedIndex {
	index := make(InvertedIndex)
	for i, d := range docx {
		for _, word := range tokenize(d) {
			if _, ok := index[word]; !ok {
				index[word] = []int{i}
			} else {
				index[word] = append(index[word], i)
				// 如果index不存在，则放入该term所在的 行数，也就是 行数
			}
		}
	}
	return index
}

// token化 调用
func tokenize(text string) []string {
	// 去除语气词
	text = removeShopWord(text)
	//调用gse库进行分词
	return globalGse.CutDAG(text)
}

// 搜索，传入参数:index-->倒排库, query：用户输出的搜索内容 docs 正排索引
func search(index InvertedIndex, query string, docs []string) ([]string, []string) {
	//set集合
	result := make(map[int]bool)
	qy := tokenize(query)     // query词条进行分词
	for _, word := range qy { // 遍历分完词的每一个term
		if doc, ok := index[word]; ok {
			// 搜索倒排索引中，term对应的doc数组，doc数组就是存在该term词条的所有的doc id
			for _, d := range doc {
				// 对doc数组进行遍历，获取所有的doc id，并且进行标志。
				result[d] = true // 存储doc id
			}
		}
	}

	var output []string
	for d := range result { // 存储 doc id
		// 利用正排索引，找到id对应的存储内容并返回
		output = append(output, docs[d])
	}
	return output, qy
}

// 实现TF-IDF
func calculateTFIDF(term string, document string, documents []string) float64 {
	tf := calculateTF(term, document)
	idf := calculateIDF(term, documents)
	return tf * idf * 100.0
}

// 计算TF
func calculateTF(term string, document string) float64 {
	termCount := strings.Count(document, term) // term 在 document中出现多少次
	totalWords := len(tokenize(document))      // 这个document有多少个词
	return float64(termCount) / float64(totalWords)
}

// 计算IDF
func calculateIDF(term string, documents []string) float64 {
	docWithTerm := 0
	for _, doc := range documents {
		if strings.Contains(doc, term) {
			docWithTerm++ // 包含term这个词的文档数
		}
	}
	return math.Log(float64(len(documents)) / float64(docWithTerm))
}

type SortRes struct {
	Docx  string
	Score float64
	Id    int
}

// 结果排序
func sortRes(qy []string, res []string) []*SortRes {
	exist := make(map[int]*SortRes)
	for _, v := range qy { // 遍历每一个query的分词后的token词条
		for i, v2 := range res { // 遍历每一个结果
			score := calculateTFIDF(v, v2, res)
			// 记录分数构成，计算每个词条对每个文档结构的score
			if _, ok := exist[i]; !ok {
				// 如果exist中还没存在这个词条，则进行进行初始化
				tmp := &SortRes{
					Docx:  v2,
					Score: score,
					Id:    i,
				}
				exist[i] = tmp
			} else {
				// 如果已经存在了，则进行分数的相加
				// 意思就是每个res中的doc对于每个token的权重之和的结果。权重的对象始终都是res中doc
				exist[i].Score += score
			}
		}
	}
	resList := make([]*SortRes, 0)
	for _, v := range exist { // 构建结构体
		resList = append(resList, &SortRes{
			Docx:  v.Docx,
			Score: v.Score,
			Id:    v.Id,
		})
	}
	//分数 从大到小排序
	sort.Slice(resList, func(i, j int) bool { // 按照score进行排序
		return resList[i].Score > resList[j].Score
	})
	return resList
}
