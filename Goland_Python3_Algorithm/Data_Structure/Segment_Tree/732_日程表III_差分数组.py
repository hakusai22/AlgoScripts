# 当 k 个日程安排有一些时间上的交叉时（例如 k 个日程安排都在同一时间内），就会产生 k 次预订。
# 给你一些日程安排 [start, end) ，请你在每个日程安排添加后，返回一个整数 k ，表示所有先前日程安排会产生的最大 k 次预订。
# 实现一个 MyCalendarThree 类来存放你的日程安排，你可以一直添加新的日程安排。
# MyCalendarThree() 初始化对象。
# int book(int start, int end) 返回一个整数 k ，表示日历中存在的 k 次预订的最大值。


from sortedcontainers import SortedDict

class MyCalendarThree:
    def __init__(self):
        self.d = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.d[start] = self.d.setdefault(start, 0) + 1
        self.d[end] = self.d.setdefault(end, 0) - 1

        ans = maxBook = 0
        for freq in self.d.values():
            maxBook += freq
            ans = max(ans, maxBook)
        return ans

if __name__ == '__main__':
    m = MyCalendarThree()
    print(m.book(10, 20))
    print(m.book(50, 60))
    print(m.book(10, 40))
    print(m.book(5, 15))
