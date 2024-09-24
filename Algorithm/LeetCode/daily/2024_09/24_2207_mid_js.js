/**
 * @param {string} text
 * @param {string} pattern
 * @return {number}
 */
var maximumSubsequenceCount = function (text, pattern) {
    const [x, y] = pattern
    let ans = 0, cntX = 0, cntY = 0
    for (const c of text) {
        if (c === y) {
            ans += cntX
            cntY++
        }
        if (c === x) {
            cntX++
        }
    }
    return ans + Math.max(cntX, cntY)
};