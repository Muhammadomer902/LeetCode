class MyCalendar(object):

    def __init__(self):
        self.calendar = [] 

    def book(self, start, end):
        for s, e in self.calendar:

            if start < e and end > s:
                return False 
        self.calendar.append((start, end))
        return True 

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start, end)
