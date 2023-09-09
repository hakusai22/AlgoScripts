# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/10 09:20
from typing import List


# 当i最开始的位置在[num, n-1]之间时，不移动本身就会对答案作出一个贡献，即diff[0]+=1；
# 当k逐渐变大时，i会向左移动出num，那个时候对答案不作出贡献了，即diff[i - num + 1] -= 1；
# 持续移动超过最左端0以后会回到n-1，又会对答案作出贡献，即diff[i + 1] += 1。
#
# 当i最开始的位置在[0, num - 1] 之间时，不移动本身不会对答案作出贡献。移动超过最左端0回到n-1，会对答案作出贡献，即diff[i + 1] += 1；
# 当继续移动，超过num回到[0, num - 1] 之间时，又不会再对答案做出贡献了，即diff[i - num + n + 1] -= 1。
#
# 我们只需要对diff进行遍历，维护每个时刻有多少个坐标满足差小于等于0，最终返回最大且最小的k即可。
#
# 作者：himymBen
# 链接：https://leetcode.cn/problems/smallest-rotation-with-highest-score/solution/pythonjavajavascriptgo-chai-fen-shu-zu-b-xhvy/


def bestRotation(nums: List[int]) -> int:
    n = len(nums)
    diff = [0] * (n + 1)
    # num ---> n - 1
    for i, num in enumerate(nums):
        if i >= num:
            diff[0] += 1
            diff[i - num + 1] -= 1
            diff[i + 1] += 1
        else:
            diff[i + 1] += 1
            diff[i - num + n + 1] -= 1
    ans = cur = mx = 0
    for i in range(n):
        cur += diff[i]
        if cur > mx:
            ans, mx = i, cur
    return ans


if __name__ == '__main__':
    bestRotation([2,3,1,4,0])
