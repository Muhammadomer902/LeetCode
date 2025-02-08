from collections import defaultdict
import sortedcontainers

class NumberContainers:
    def __init__(self):
        self.index_to_number = {}  # Maps index to number
        self.number_to_indices = defaultdict(sortedcontainers.SortedSet)  # Maps number to a sorted set of indices

    def change(self, index, number):
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            if old_number != number:
                self.number_to_indices[old_number].discard(index)
                if not self.number_to_indices[old_number]:
                    del self.number_to_indices[old_number]
        
        self.index_to_number[index] = number
        self.number_to_indices[number].add(index)

    def find(self, number):
        if number in self.number_to_indices and self.number_to_indices[number]:
            return self.number_to_indices[number][0]
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)