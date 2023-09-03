'''
Author: hakusai
Date: 2023-04-22 17:37:10
LastEditTime: 2023-04-23 10:22:01
'''


from typing import List


class Solution:
    def adventureCamp(self, a: List[str]) -> int:
        n = len(a)
        st = set()
        for i in a[0].split('->'):
            st.add(i)
        ans = -1
        mx = 0
        for i in range(1, n):
            cur = 0
            for j in a[i].split('->'):
                if j and j not in st:
                    st.add(j)
                    cur += 1
            if cur > mx:
                mx = cur
                ans = i
        return ans


if __name__ == "__main__":
    print(Solution().adventureCamp(["1"]))
