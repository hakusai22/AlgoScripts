/**
 * @Time 2024/10/01 23:50
 * @Author  : https://github.com/hakusai22
 * @题目     :
 * @参考     :
 * @时间复杂度:
 * @空间复杂度:
 */

/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function (n) {
    return n > 0 && (n & (n - 1)) === 0 && (n % 3 === 1);
};