# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = ListNode(-101)
        if not head:
            return None
        elif head.next==None:
            return head
        while head.next!=None:
            if head.val==head.next.val:
                val = head.val
                while head and head.val==val:
                    head=head.next
                if not head and temp.val==-101:
                    return None
                elif not head and temp:
                    return temp
                continue
            elif temp.val==-101:
                temp = ListNode(head.val)
            else:
                iter = temp
                while iter.next!=None:
                    iter=iter.next
                iter.next = ListNode(head.val)
            head = head.next
            print(temp)
        if temp.val==-101:
            return ListNode(head.val)
        iter = temp
        while iter.next!=None:
            iter=iter.next
        iter.next = ListNode(head.val)
        return temp