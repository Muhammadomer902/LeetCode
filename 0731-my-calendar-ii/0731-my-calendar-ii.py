class MyCalendarTwo(object):

    def __init__(self):
        self.booked = [] 
        self.double_booked = []  

    def book(self, start, end):
        for s, e in self.double_booked:
            if start < e and end > s:
                return False
        for s, e in self.booked:
            if start < e and end > s:
                overlap_start = max(start, s)
                overlap_end = min(end, e)
                self.double_booked.append((overlap_start, overlap_end))

        self.booked.append((start, end))
        return True 

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start, end)

        