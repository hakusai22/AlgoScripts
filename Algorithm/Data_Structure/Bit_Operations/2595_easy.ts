/**
 * @Time 2024/10/01 23:30
 * @Author  : https://github.com/hakusai22
 */

function evenOddBit(n: number): number[] {
    let ans: number[] = [0, 0];
    for (let i = 0; i < 32; i++) {
        if ((n >> i) & 1) {
            ans[i % 2] = ans[i % 2] + 1;
        }
    }
    return ans;
}