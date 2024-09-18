function longestContinuousSubstring(s: string): number {
    let ans: number = 1, cnt: number = 1;
    for (let i: number = 1; i < s.length; i++) {
        if (s.charCodeAt(i - 1) + 1 === s.charCodeAt(i)) {
            ans = Math.max(ans, ++cnt);
        } else {
            cnt = 1;
        }
    }
    return ans;
}