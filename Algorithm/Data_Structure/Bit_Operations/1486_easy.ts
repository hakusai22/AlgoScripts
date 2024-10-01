/**
 * @Time 2024/10/01 23:40
 * @Author  : https://github.com/hakusai22
 * @题目     :
 * @参考     :
 * @时间复杂度:
 * @空间复杂度:
 */

function xorOperation(n: number, start: number): number {
    let ans = 0;
    for (let i = 0; i < n; i++) {
        ans ^= (start + 2 * i);
    }
    return ans;
};