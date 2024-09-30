class CustomStack:

    def __init__(self, maxSize):
        self.stack = []
        self.maxSize = maxSize
        self.incremental = [0] * maxSize

    def push(self, x):
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self):
        if not self.stack:
            return -1
        idx = len(self.stack) - 1
        res = self.stack.pop() + self.incremental[idx]
        if idx > 0:
            self.incremental[idx - 1] += self.incremental[idx]
        self.incremental[idx] = 0  
        return res

    def increment(self, k, val):
        if self.stack:
            idx = min(k, len(self.stack)) - 1
            self.incremental[idx] += val
