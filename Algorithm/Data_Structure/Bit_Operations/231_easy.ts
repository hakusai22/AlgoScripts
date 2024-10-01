/**
 * @Time 2024/10/01 23:42
 * @Author  : https://github.com/hakusai22
 * @题目     : https://leetcode.cn/problems/power-of-two/description/
 * @参考     :
 * @时间复杂度:
 * @空间复杂度:
 */

function isPowerOfTwo(n: number): boolean {
    return n > 0 && (n & (n - 1)) === 0;
};