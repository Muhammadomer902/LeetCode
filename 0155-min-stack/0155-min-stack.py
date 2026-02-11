class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            size=len(self.minStack)
            self.minStack.append(min(val,self.minStack[size-1]))
        

    def pop(self):
        """
        :rtype: None
        """
        size=len(self.stack)
        self.stack = self.stack[:size-1]
        self.minStack =self.minStack[:size-1]

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
        size=len(self.stack)
        return self.minStack[size-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()