/*
 * @Author: hakusai
 * @Date: 2023-05-17 23:20:15
 * @LastEditTime: 2023-05-17 23:52:55
 * @Description:
 */
package 单元测试入门

func addNumber(num int) int {
	res := 0
	for i := 0; i < num; i++ {
		res += i
	}
	return res
}
