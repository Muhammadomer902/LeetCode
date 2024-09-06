# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums_set = set(nums)
        start = ListNode(0)
        start.next = head
        cur = head
        prev = start;
        while cur:
            if cur.val in nums_set:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return start.next

        