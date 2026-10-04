# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None and list2 is None:

            return None
        
        if list1 is None:

            return list2
        
        if list2 is None:

            return list1
        
        curr = None

        if list1.val <= list2.val:

            curr = list1
            list1 = list1.next
        
        else:

            curr = list2
            list2 = list2.next
        
        newhead = curr

        while list1 is not None and list2 is not None:

            if list1.val <= list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
        
        if list1 is not None:

            curr.next = list1
        
        else:
            curr.next = list2
        
        return newhead







        