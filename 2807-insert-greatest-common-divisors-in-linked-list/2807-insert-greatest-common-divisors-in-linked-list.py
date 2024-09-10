# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def greatestCommonDivisor(self,num1,num2):
        while num2:
            num1, num2 = num2, num1 % num2
        return num1

    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = head
        while cur.next!=None:
            gcd_val = self.greatestCommonDivisor(cur.val, cur.next.val)
            cur.next = ListNode(gcd_val, cur.next)
            cur = cur.next.next
        return head