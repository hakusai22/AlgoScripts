var findTheCity = function (n, edges, distanceThreshold) {
    const w = Array(n).fill(null).map(() => Array(n).fill(Infinity));
    for (const [x, y, wt] of edges) {
        w[x][y] = w[y][x] = wt;
    }

    const memo = new Array(n).fill(null).map(() => new Array(n).fill(null).map(() => new Array(n).fill(0)));
    function dfs(k, i, j) {
        if (k < 0) { // 递归边界
            return w[i][j];
        }
        if (memo[k][i][j]) { // 之前计算过
            return memo[k][i][j];
        }
        return memo[k][i][j] = Math.min(dfs(k - 1, i, j), dfs(k - 1, i, k) + dfs(k - 1, k, j));
    }

    let ans = 0;
    let minCnt = n;
    for (let i = 0; i < n; i++) {
        let cnt = 0;
        for (let j = 0; j < n; j++) {
            if (j !== i && dfs(n - 1, i, j) <= distanceThreshold) {
                cnt++;
            }
        }
        if (cnt <= minCnt) { // 相等时取最大的 i
            minCnt = cnt;
            ans = i;
        }
    }
    return ans;
};
