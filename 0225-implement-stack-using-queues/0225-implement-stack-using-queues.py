class MyStack(object):

    def __init__(self):
        self.q = []
        self.q1 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.q:
            self.q.append(x)
        else:
            self.q1 = self.q
            self.q = [x]
            self.q.extend(self.q1)        

    def pop(self):
        """
        :rtype: int
        """
        if self.q:
            self.q1 = self.q
            self.q = self.q[1:]
            return self.q1[0]
        

    def top(self):
        """
        :rtype: int
        """
        return self.q[0]

    def empty(self):
        """
        :rtype: bool
        """
        if self.q:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()