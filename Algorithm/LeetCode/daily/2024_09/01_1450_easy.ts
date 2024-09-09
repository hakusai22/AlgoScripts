/**
 * @Time 2024/09/09 22:35
 * @Author  : https://github.com/hakusai22
 */


function busyStudent(startTime: number[], endTime: number[], queryTime: number): number {
    var n = startTime.length;
    let ans = 0
    for (let i = 0; i < n; i++) {
        if (startTime[i] <= queryTime && queryTime <= endTime[i]) {
            ans++;
        }
    }
    return ans;
}