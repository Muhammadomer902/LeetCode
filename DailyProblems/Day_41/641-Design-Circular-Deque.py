class MyCircularDeque:

    def __init__(self, k):
        """
        Initialize the deque with a maximum size of k.
        """
        self.k = k
        self.deque = [0] * k  # Circular array for the deque
        self.front = 0  # Points to the front element
        self.rear = 0  # Points to the next position where the rear element will be inserted
        self.size = 0  # Current number of elements in the deque

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return True if the operation is successful, False otherwise.
        """
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.k  # Move front pointer backward
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return True if the operation is successful, False otherwise.
        """
        if self.isFull():
            return False
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.k  # Move rear pointer forward
        self.size += 1
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return True if the operation is successful, False otherwise.
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k  # Move front pointer forward
        self.size -= 1
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return True if the operation is successful, False otherwise.
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.k  # Move rear pointer backward
        self.size -= 1
        return True

    def getFront(self):
        """
        Gets the front item from the deque. Return -1 if the deque is empty.
        """
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self):
        """
        Gets the last item from the deque. Return -1 if the deque is empty.
        """
        if self.isEmpty():
            return -1
        return self.deque[(self.rear - 1) % self.k]

    def isEmpty(self):
        """
        Checks whether the deque is empty or not.
        """
        return self.size == 0

    def isFull(self):
        """
        Checks whether the deque is full or not.
        """
        return self.size == self.k



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()