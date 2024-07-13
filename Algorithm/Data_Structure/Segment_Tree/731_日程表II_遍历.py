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

# 记录下所有已经预定的课程安排区间与已经预定过两次的课程安排区间，
# 当我们预定新的区间 [start,end) 时，此时检查当前已经预定过两次的每个日程安排是否与新日程安排冲突。
# 若不冲突，则可以添加新的日程安排。

class MyCalendarTwo:
    def __init__(self):
        self.booked = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        if any(s < end and start < e for s, e in self.overlaps):
            return False
        for s, e in self.booked:
            if s < end and start < e:
                self.overlaps.append((max(s, start), min(e, end)))
        self.booked.append((start, end))
        return True
