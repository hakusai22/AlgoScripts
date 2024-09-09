/**
 * @Time 2024/09/09 22:41
 * @Author  : https://github.com/hakusai22
 */

function maxConsecutiveAnswers(answerKey: string, k: number): number {
    let ans = 0, left = 0;
    const cnt = [0, 0];
    for (let right = 0; right < answerKey.length; right++) {
        cnt[answerKey[right].charCodeAt(0) >> 1 & 1]++;
        while (cnt[0] > k && cnt[1] > k) {
            cnt[answerKey[left++].charCodeAt(0) >> 1 & 1]--;
        }
        ans = Math.max(ans, right - left + 1);
    }
    return ans;
};