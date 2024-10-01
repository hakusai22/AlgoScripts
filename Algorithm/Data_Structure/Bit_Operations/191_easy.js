/**
 * @Time 2024/10/01 15:43
 * @Author  : https://github.com/hakusai22
 */

/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function (n) {
    let count = 0
    while (n) {
        if (n & 1) {
            count++
        }
        n = n >>> 1
    }
    return count
}

