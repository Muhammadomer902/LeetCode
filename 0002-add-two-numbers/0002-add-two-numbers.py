# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addToList(self, val, list):
        temp = ListNode(val)
        while list.next!=None:
            list = list.next
        list.next = temp

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num1 = 0;num2 = 0;i=1
        while l1!=None:
            num1 = num1+l1.val*i
            l1 = l1.next;i*=10
        i=1
        while l2!=None:
            num2 = num2+l2.val*i
            l2 = l2.next;i*=10
        rnum = num1+num2
        digit = rnum%10
        rnum = int(rnum/10)
        rlist = ListNode(digit)
        while rnum:
            digit = rnum%10
            rnum = int(rnum/10)
            self.addToList(digit,rlist)
            # temp = ListNode(digit)
            # rlist.next = temp
            # rlist = rlist.next
        return rlist