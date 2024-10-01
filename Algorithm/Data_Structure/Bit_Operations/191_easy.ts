/**
 * @Time 2024/10/01 15:45
 * @Author  : https://github.com/hakusai22
 */

function hammingWeight(n: number): number {
    let count = 0
    while (n) {
        if (n & 1) {
            count++
        }
        n = n >>> 1
    }
    return count
};