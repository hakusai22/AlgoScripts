MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')
INFMAX = float('inf')

# -*- coding: utf-8 -*-
# @Author  : wheat
# @Time    : 2023/01/13 16:58

if __name__ == '__main__':

    def qmi(a, k, p):
        ans = 1
        while k:
            if k & 1 == 1:
                ans = ans * a % p
            k >>= 1
            a = a ** 2 % p
        return ans

    if __name__ == "__main__":
        n = int(input())
        a, b, ans = 2 * n, n, 1
        for i in range(a, a - b, -1):
            ans = ans * i % MOD
        for i in range(1, b + 1):
            ans = ans * qmi(i, MOD - 2, MOD) % MOD

        ans = ans * qmi(n + 1, MOD - 2, MOD) % MOD
        print(ans)
