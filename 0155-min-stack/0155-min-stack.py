class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        size=len(self.stack)
        self.stack = self.stack[:size-1]

    def top(self):
        """
        :rtype: int
        """
        size=len(self.stack)
        return self.stack[size-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()