# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        current = head
        total_length = 0
        while current:
            total_length += 1
            current = current.next

        part_length = total_length // k
        remainder = total_length % k

        parts = [None] * k 
        current = head
        
        for i in range(k):
            if current:
                parts[i] = current
                current_part_size = part_length + (1 if i < remainder else 0)
                for j in range(current_part_size - 1):
                    if current:
                        current = current.next
                
                if current:
                    next_part = current.next
                    current.next = None
                    current = next_part
        
        return parts