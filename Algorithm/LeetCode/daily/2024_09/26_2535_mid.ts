/**
 * @Time 2024/09/26 14:23
 * @Author  : https://github.com/hakusai22
 */

function differenceOfSum(nums: number[]): number {
    let ans = 0
    for (let num of nums) {
        ans += num
        while (num) {
            ans -= num % 10
            num = Math.floor(num / 10)
        }
    }
    return ans
}