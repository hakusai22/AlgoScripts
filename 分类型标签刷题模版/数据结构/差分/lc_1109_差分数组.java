/*
 * @Author: hakusai
 * @Date: 2022-06-25 12:36:47
 * @LastEditTime: 2023-05-16 22:49:15
 * @Description: 
 */
package 分类型标签刷题模版.数据结构.差分;

class lc_1109_差分数组 {
    public int[] corpFlightBookings(int[][] bs, int n) {
        int[] c = new int[n + 1];
        for (int[] bo : bs) {
            int l = bo[0] - 1, r = bo[1] - 1, v = bo[2];
            c[l] += v;
            c[r + 1] -= v;
        }
        int[] ans = new int[n];
        ans[0] = c[0];
        for (int i = 1; i < n; i++) {
            ans[i] = ans[i - 1] + c[i];
        }
        return ans;
    }
}
