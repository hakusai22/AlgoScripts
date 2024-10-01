/**
 * @Time 2024/10/01 23:30
 * @Author  : https://github.com/hakusai22
 */

/**
 * @param {number} n
 * @return {number[]}
 */
var evenOddBit = function (n) {
    let ans = [0, 0];
    let i = 0;
    while (n) {
        if (n & 1) ans[i % 2]++;
        i++;
        n >>= 1;
    }
    return ans;
};