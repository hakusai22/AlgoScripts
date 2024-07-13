package main

import (
	"fmt"
)

type Node struct {
	letter rune
	next   map[rune]*Node
	isWord bool
}

type Tire struct {
	Head *Node
}

func NewTire() *Tire {
	return &Tire{
		Head: &Node{
			letter: '-',
			next:   make(map[rune]*Node),
			isWord: false,
		},
	}
}

func (t *Tire) InsertWord(word string) {
	head := t.Head
	for i, s := range word {
		if head.next[s] == nil {
			head.next[s] = &Node{
				letter: s,
				next:   make(map[rune]*Node),
				isWord: false,
			}
			if i == len(word)-1 {
				head.next[s].isWord = true
			}
		}
		head = head.next[s]
	}
}

func (t *Tire) Search(word string) bool {
	head := t.Head
	for _, s := range word {
		if head.next[s] == nil {
			return false
		}
		head = head.next[s]
	}
	return head.isWord
}

func (t *Tire) GetAllWords(word string) []string {
	head := t.Head
	for _, s := range word {
		if head.next[s] == nil {
			return []string{}
		}
		head = head.next[s]
	}

	res := make([]string, len(head.next))
	//遍历

	return t.dfs(head, word, res)
}

func (t *Tire) dfs(node *Node, p string, res []string) []string {
	if node.isWord {
		return append(res, p)
	}
	for _, l := range node.next {
		res = t.dfs(l, p+string(l.letter), res)
	}
	return res
}

func main() {
	tire := NewTire()
	tire.InsertWord("hello")
	tire.InsertWord("help")
	fmt.Println(tire.Search("hello1"))
	fmt.Println(tire.GetAllWords("hell"))
}
