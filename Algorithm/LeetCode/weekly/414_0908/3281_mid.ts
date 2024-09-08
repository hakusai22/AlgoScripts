/**
 * @Time 2024/09/08 15:38
 * @Author  : https://github.com/hakusai22
 * 给你一个整数数组 start 和一个整数 d，代表 n 个区间 [start[i], start[i] + d]。
 * 你需要选择 n 个整数，其中第 i 个整数必须属于第 i 个区间。所选整数的 得分 定义为所选整数两两之间的 最小 绝对差。
 * 返回所选整数的 最大可能得分 。
 *
 * 2 <= start.length <= 10^5
 * 0 <= start[i] <= 10^9
 * 0 <= d <= 10^9
 */

function maxPossibleScore(start: number[], d: number): number {
    start.sort((a, b) => a - b);  // Sort the array

    function check(score: number): boolean {
        let preX = -Infinity;  // Initial value for preX

        for (let s of start) {
            let x = preX + score;
            if (x > s + d) {
                return false;
            }
            preX = Math.max(x, s);
        }
        return true;
    }

    let left = 0;
    let right = (start[start.length - 1] + d - start[0]) + 1

    while (left + 1 < right) {
        const mid = Math.floor((left + right) / 2);
        if (check(mid)) {
            left = mid;
        } else {
            right = mid;
        }
    }
    return left;
}
