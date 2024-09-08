/**
 * @Time 2024/09/08 15:41
 * @Author  : https://github.com/hakusai22
 *
 * 给你一个长度为 n 的整数数组 nums 。
 * 你的目标是从下标 0 出发，到达下标 n - 1 处。每次你只能移动到 更大 的下标处。
 * 从下标 i 跳到下标 j 的得分为 (j - i) * nums[i] 。
 * 请你返回你到达最后一个下标处能得到的 最大总得分 。
 *
 *
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^5
 */


function findMaximumScore(nums: number[]): number {
    let ans = 0
    let max = nums[0];
    for (let i = 0; i < nums.length - 1; i++) {
        max = Math.max(nums[i], max)
        ans += max
    }
    return ans
}

console.log(findMaximumScore([1, 3, 1, 5]))