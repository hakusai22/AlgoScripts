/**
 * @Time 2024/10/01 15:39
 * @Author  : https://github.com/hakusai22
 * https://leetcode.cn/problems/xor-operation-in-an-array/description/
 */

/**
 * @param {number} n
 * @param {number} start
 * @return {number}
 */
var xorOperation = function (n, start) {
    let ans = start
    for (let i = 1; i < n; i++) {
        ans = ans ^ (start + 2 * i)
    }
    return ans
};

