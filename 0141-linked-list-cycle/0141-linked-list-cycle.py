# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        arr = [];count = 0;i = head
        if not i:
            return False
        while i.next!=None:
            if i not in arr:
                arr.append(i)
                count+=1
            else:
                return True
            i = i.next
        return False