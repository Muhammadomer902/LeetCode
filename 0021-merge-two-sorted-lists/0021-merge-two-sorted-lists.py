# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 and not list2:
            return None
        
        merged = ListNode()
        tempMer = merged

        while list1 or list2:
            if list1 and list2 and list1.val<=list2.val:
                temp = ListNode(list1.val)
                tempMer.next = temp
                tempMer = tempMer.next
                list1 = list1.next
            elif list1 and list2 and list2.val<=list1.val:
                temp = ListNode(list2.val)
                tempMer.next = temp
                tempMer = tempMer.next
                list2 = list2.next
            elif list1 and not list2:
                temp = ListNode(list1.val)
                tempMer.next = temp
                tempMer = tempMer.next
                list1 = list1.next
            elif list2 and not list1:
                temp = ListNode(list2.val)
                tempMer.next = temp
                tempMer = tempMer.next
                list2 = list2.next
        
        return merged.next