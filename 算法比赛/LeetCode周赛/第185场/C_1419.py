# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/23 21:10


# c,r,o,a,k分别表示遍历到当前位置时这几个字母出现的次数。
# 每次遍历过程中当且仅当c>=r>=o>=a>=k时才符合要求。
# now表示当前存在的青蛙个数，即遇到c时加一，叫完以后(遇到k)减一。
# 遍历完后now应为0表示每次叫声都有头有尾，记录now的最大值即为答案。


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c = r = o = a = k = 0
        now = 0
        res = 0
        for i in croakOfFrogs:
            if i == 'c':
                c += 1
                now += 1
                res = max(res, now)
            elif i == 'r':
                r += 1
            elif i == 'o':
                o += 1
            elif i == 'a':
                a += 1
            elif i == 'k':
                k += 1
                now -= 1
            if not c >= r >= o >= a >= k:
                return -1
        return res if now == 0 else -1


if __name__ == '__main__':
    print(Solution().minNumberOfFrogs("croakcroak"))
