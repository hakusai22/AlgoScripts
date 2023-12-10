# 当 k 个日程安排有一些时间上的交叉时（例如 k 个日程安排都在同一时间内），就会产生 k 次预订。
# 给你一些日程安排 [start, end) ，请你在每个日程安排添加后，返回一个整数 k ，表示所有先前日程安排会产生的最大 k 次预订。
# 实现一个 MyCalendarThree 类来存放你的日程安排，你可以一直添加新的日程安排。
# MyCalendarThree() 初始化对象。
# int book(int start, int end) 返回一个整数 k ，表示日历中存在的 k 次预订的最大值。


# 利用线段树，假设我们开辟了数组 arr[0,⋯,109]
#  ，初始时每个元素的值都为 0，对于每次行程预定的区间 [start,end) ，
#  则我们将区间中的元素 arr[start,⋯,end−1]中的每个元素加 1，
#  最终只需要求出数组 arr的最大元素即可。实际我们不必实际开辟数组 arr，
#  可采用动态线段树，懒标记 lazy\textit{lazy}lazy 标记区间 [l,r] 进行累加的次数，
#  tree记录区间 [l,r]的最大值，最终返回区间 [0,10^9] 中的最大元素即可。

from collections import defaultdict

class MyCalendarThree:
    def __init__(self):
        self.tree = defaultdict(int)
        self.lazy = defaultdict(int)

    def update(self, start: int, end: int, l: int, r: int, idx: int):
        if r < start or end < l:
            return
        if start <= l and r <= end:
            self.tree[idx] += 1
            self.lazy[idx] += 1
        else:
            mid = (l + r) // 2
            self.update(start, end, l, mid, idx * 2)
            self.update(start, end, mid + 1, r, idx * 2 + 1)
            self.tree[idx] = self.lazy[idx] + max(self.tree[idx * 2], self.tree[idx * 2 + 1])

    def book(self, start: int, end: int) -> int:
        self.update(start, end - 1, 0, 10 ** 9, 1)
        return self.tree[1]


