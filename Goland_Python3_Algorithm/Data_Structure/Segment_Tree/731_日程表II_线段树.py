# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/30 08:39

# 实现一个 MyCalendar 类来存放你的日程安排。如果要添加的时间内不会导致三重预订时，则可以存储这个新的日程安排。
# MyCalendar 有一个 book(int start, int end)方法。它意味着在 start 到 end 时间内增加一个日程安排，
# 注意，这里的时间是半开区间，即 [start, end), 实数 x 的范围为，  start <= x < end。
# 当三个日程安排有一些时间上的交叉时（例如三个日程安排都在同一时间内），就会产生三重预订。
# 每次调用 MyCalendar.book方法时，如果可以将日程安排成功添加到日历中而不会导致三重预订，返回 true。
# 否则，返回 false 并且不要将该日程安排添加到日历中。
# 请按照以下步骤调用MyCalendar 类: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

# 利用线段树，假设我们开辟了数组 arr[0,⋯,109]，初始时每个元素的值都为 0，
# 对于每次行程预定的区间 [start,end) ，则我们将区间中的元素 arr[start,⋯,end−1] 中的每个元素加 1，
# 如果数组 arr 的最大元素大于 2 时，此时则出现某个区间被安排了 2 次上，此时返回 false，
# 同时将数组区间 arr[start,⋯,end−1] 进行减 111 即可恢复。
# 实际我们不必实际开辟数组 arr，可采用动态线段树，懒标记 lazy 标记区间 [l,r] 进行累加的次数，
# tree 记录区间 [l,r] 的最大值，每次动态更新线段树即可。

# 时间复杂度：O(nlogC) 其中 n 为日程安排的数量。由于使用了线段树查询，线段树的最大深度为 ClogC  C 取固定值即为 10^9

class MyCalendarTwo:
    def __init__(self):
        self.tree = {}

    def update(self, start: int, end: int, val: int, l: int, r: int, idx: int) -> None:
        if r < start or end < l:
            return
        if start <= l and r <= end:
            p = self.tree.get(idx, [0, 0])
            p[0] += val
            p[1] += val
            self.tree[idx] = p
            return
        mid = (l + r) // 2
        self.update(start, end, val, l, mid, 2 * idx)
        self.update(start, end, val, mid + 1, r, 2 * idx + 1)
        p = self.tree.get(idx, [0, 0])
        p[0] = p[1] + max(self.tree.get(2 * idx, (0,))[0], self.tree.get(2 * idx + 1, (0,))[0])
        self.tree[idx] = p

    def book(self, start: int, end: int) -> bool:
        self.update(start, end - 1, 1, 0, 10 ** 9, 1)
        if self.tree[1][0] > 2:
            self.update(start, end - 1, -1, 0, 10 ** 9, 1)
            return False
        return True
