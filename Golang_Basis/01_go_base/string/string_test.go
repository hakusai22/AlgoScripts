/*
 * @Author: hakusai
 * @Date: 2023-05-17 16:41:18
 * @LastEditTime: 2023-05-17 16:46:13
 * @Description:
 */

package string_test

import (
	"fmt"
	"strconv"
	"strings"
	"testing"
)

func TestString(t *testing.T) {
	case_test()
}

func case_test() {
	case_1()
	case_2()
	case_3()
	case_4()
	case_5()
	case_6()
	case_8()
	case_9()
	case_10()
	case_11()
	case_12()
	case_13()
	case_14()
	case_15()
	case_16()
	case_17()
}

/*
*
字符串转整数
strconv.Atoi()函数用来将字符串转为整数，括号里填要转整数的字符串
*/
func case_1() {
	number, err := strconv.Atoi("1234") //number接收转换后的整数，err接收转换失败的原因
	if err != nil {                     //err不为空，发生错误，转换失败
		fmt.Println("发生错误：", err) //转换失败时number为默认值0
	} else { //err为空表示转换无错误，转换成功
		fmt.Println(number)
	}
}

/*
*
整数转字符串
strconv.Itoa()函数整数转字符串，函数里填要转为字符串的整数
*/
func case_2() {
	str := strconv.Itoa(-123) //函数只有一个返回值，str接收转换后的字符串；整数转字符串必转成功不会发生错误，因此没有错误原因返回值
	fmt.Printf("转换结果：%v    数据类型：%T", str, str)
}

/*
*
字符串转切片
slice := []byte()函数将字符串转为切片，转换为byte数据类型的切片，括号里写要转为切片的字符串
*/
func case_3() {
	slice := []byte("hello golang!") //slice接收转换后的切片,字符串转切片必转成功不会发生错误
	//切片存储的元素为字符串中各字符在UTF-8表中的十进制表示，查看字符需要再转换为UTF-8表中十进制对应的字符
	fmt.Printf("转换结果：%v\n对应ASCII码表的字符：%c\n数据类型：%T", slice, slice, slice)
}

/*
*
切片转字符串
str := string()函数将切片转为字符串，括号里写要转为字符串的切片，切片的数据类型为byte
切片元素为十进制UTF-8表的整数，转换后的字符串为UTF-8表整数对应的字符
*/
func case_4() {
	str := string([]byte{104, 101, 108, 108, 111, 32, 103, 111, 108, 97, 110, 103, 33}) //str接收转换后的字符串
	fmt.Printf("转换结果：%v    数据类型：%T", str, str)
}

/*
*
十进制转换为其他进制
strconv.FormatInt()函数将十进制转为其他进制  括号里两个参数:第一个参数为要转的十进制数，第二个参数为要转的进制
函数返回值一个,为转换结果
*/
func case_5() {
	var number int64 = 565643
	base_2 := strconv.FormatInt(number, 2)
	base_8 := strconv.FormatInt(number, 8)
	base_16 := strconv.FormatInt(number, 16)
	fmt.Print("十进制：", number, "\n转为二进制：", base_2, "\n转为八进制：", base_8, "\n转为十六进制：", base_16)
}

/*
*
字符串转为大写或小写
strings.ToLower()函数：字符串转为小写  一个参数：要转的原字符串  一个返回值：转换后的新字符串
strings.ToUpper()函数：字符串转为大写  一个参数：要转的原字符串  一个返回值：转换后的新字符串
*/
func case_6() {
	str := "hello golang!"
	fmt.Println(strings.ToLower(str)) //转为小写
	fmt.Println(strings.ToUpper(str)) //转为大写
}

/*
*
字符串比较
strings.EqualFold() 比较字符串是否相同，不区分大小写，两个参数:两个要比较的字符串
返回值一个：返回比较结果，相同为true，不相同false
比较字符串是否相同并区分大小写用“==”比较，返回值一个：返回比较结果，相同为true，不相同false
*/
func case_8() {
	result_1 := strings.EqualFold("abc", "Abc")
	fmt.Printf("“strings.EqualFold”的比较结果：%v    数据类型：%T\n", result_1, result_1)
	result_2 := "abc" == "Abc"
	fmt.Printf("“==”的比较结果：%v    数据类型：%T", result_2, result_2)
}

/*
*
字符串是否包含子字符串
strings.Contains()函数  两个参数：第一个参数 字符串，第二个参数 子字符串
函数返回值一个：布尔值，包含就返回true，不包含返回false
*/
func case_9() {
	result := strings.Contains("hello golang!", "ll")
	fmt.Printf("结果：%v    数据类型：%T", result, result)
}

/*
*
统计字符串中子字符串出现的次数
strings.Contains()函数  两个参数：第一个参数 字符串，第二个参数 要统计的子字符串
函数返回值一个：子字符串出现的次数
*/
func case_10() {
	result := strings.Count("hello golang!", "l")
	fmt.Printf("结果：%v    数据类型：%T", result, result)
}

/*
*
字符串在字符串中出现的下标，没有就返回-1
strings.Index()函数计算子字符串在字符串中首次出现的下标  一个返回值：返回值为子字符串出现的下标，没有出现为-1
strings.LastIndex()函数计算子字符串在字符串中最后一次出现的下标  一个返回值：返回值为子字符串出现的下标，没有出现为-1
两个函数都是两个参数：第一个为字符串，第二个为要计算的子字符串
*/
func case_11() {
	//首次出现
	sub_start := strings.Index("hello golang!", "ll")
	fmt.Println(sub_start)
	//最后一次出现
	sub_end := strings.LastIndex("hello golang!", "an")
	fmt.Println(sub_end)
}

/*
*
判断字符串是否以指定子字符串开头和结尾
strings.HasPrefix()函数：判断字符串是否以指定子字符串开头  两个参数：第一个为原字符串，第二个为要判断的子字符串  一个返回值：判断结果，布尔值
strings.TrimLeft()函数：判断字符串是否以指定子字符串结尾  两个参数：第一个为原字符串，第二个为要判断的子字符串  一个返回值：判断结果，布尔值
*/
func case_12() {
	str := "hello golang!"
	fmt.Printf("结果：%v   数据类型：%T\n", strings.HasPrefix(str, "he"), strings.HasPrefix(str, "he")) //是否以指定字符开头
	fmt.Printf("结果：%v   数据类型：%T", strings.HasSuffix(str, "png"), strings.HasSuffix(str, "e!"))  //是否以指定字符结尾
}

/*
*
遍历字符串
将字符串转为切片存入切片中，遍历切片
*/
func case_13() {
	str := "你好 golang!"
	slice := []rune(str) //字符串转为切片
	fmt.Println("slice：", slice, len(slice), cap(slice))
	for i := 0; i < len(slice); i++ {
		fmt.Printf("%c\n", slice[i]) //切片存储的元素为字符串中各字符在UTF-8表中的十进制表示，遍历原字符要将各十进制元素再转为在UTF-8表中字符表示形式
	}
}

func case_14() {
	str := strings.Replace("go go go go 语言", "go", "goland", 2)
	fmt.Println(str)
}

func case_15() {
	array := strings.Split("dsaf asdf asdfa asdf", " ")
	fmt.Printf("替换后：%v   数据类型：%T", array, array)
}

/*
*
字符串去前后空格
strings.TrimSpace()函数：字符串去前后空格  一个参数：要处理的原字符串  一个返回值：处理后的新字符串
*/
func case_16() {
	str := " hello golang!  "
	fmt.Println(strings.TrimSpace(str))
}

/*
*
去除字符串开头或结尾指定子字符串
strings.Trim()函数：去除字符串开头和结尾指定子字符串  两个参数：第一个为原字符串，第二个为字符串中要去的子字符串  一个返回值：处理后的新字符串
strings.TrimLeft()函数：去除字符串开头指定子字符串  两个参数：第一个为原字符串，第二个为字符串中要去的子字符串  一个返回值：处理后的新字符串
strings.TrimRight()函数：去除字符串结尾指定子字符串  两个参数：第一个为原字符串，第二个为字符串中要去的子字符串  一个返回值：处理后的新字符串
*/
func case_17() {
	str := "!hello golang!"
	fmt.Println(strings.Trim(str, "!"))       //去除开头和结尾指定字符
	fmt.Println(strings.TrimLeft(str, "!he")) //去除开头指定字符
	fmt.Println(strings.TrimRight(str, "g!")) //去除结尾指定字符
}
