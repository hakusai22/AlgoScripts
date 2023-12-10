# 利用线段树，假设我们开辟了数组 arr[0,⋯,109]，初始时每个元素的值都为 0，
# 对于每次行程预订的区间 [start,end)，则我们将区间中的元素 arr[start,⋯,end−1]中的每个元素都标记为 1，
# 每次调用 book时，我们只需要检测 arr[start,⋯,end−1]区间内是否有元素被标记为 1。
# 实际我们不必实际开辟数组 arr，可采用动态线段树，懒标记 lazy 标记区间 [l,r]已经被预订，
# tree 记录区间 [l,r] 的是否存在标记为 1 的元素。

# 时间复杂度：O(nlogC) 其中 n 为日程安排的数量。由于使用了线段树查询，线段树的最大深度为 ClogC  C 取固定值即为 10^9
#
class MyCalendar:
    def __init__(self):
        self.tree = set()
        self.lazy = set()

    def query(self, start: int, end: int, l: int, r: int, idx: int) -> bool:
        if r < start or end < l:
            return False
        if idx in self.lazy:  # 如果该区间已被预订，则直接返回
            return True
        if start <= l and r <= end:
            return idx in self.tree
        mid = (l + r) // 2
        return self.query(start, end, l, mid, 2 * idx) or \
               self.query(start, end, mid + 1, r, 2 * idx + 1)

    def update(self, start: int, end: int, l: int, r: int, idx: int) -> None:
        if r < start or end < l:
            return
        if start <= l and r <= end:
            self.tree.add(idx)
            self.lazy.add(idx)
        else:
            mid = (l + r) // 2
            self.update(start, end, l, mid, 2 * idx)
            self.update(start, end, mid + 1, r, 2 * idx + 1)
            self.tree.add(idx)
            if 2 * idx in self.lazy and 2 * idx + 1 in self.lazy:
                self.lazy.add(idx)

    def book(self, start: int, end: int) -> bool:
        if self.query(start, end - 1, 0, 10 ** 9, 1):
            return False
        self.update(start, end - 1, 0, 10 ** 9, 1)
        return True
