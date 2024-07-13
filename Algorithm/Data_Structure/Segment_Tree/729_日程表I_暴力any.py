
class MyCalendar:
    def __init__(self):
        self.booked = []

    def book(self, start: int, end: int) -> bool:
        if any(l < end and start < r for l, r in self.booked):
            return False
        self.booked.append((start, end))
        return True
