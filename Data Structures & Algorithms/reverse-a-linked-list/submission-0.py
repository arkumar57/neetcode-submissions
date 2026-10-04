# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:

            return None
        


        mystack = []

        curr = head

        while curr is not None:

            mystack.append(curr)
            curr = curr.next
        
        newNode = mystack.pop()

        newhead = newNode

        while mystack:

            newNode.next = mystack.pop()

            newNode = newNode.next
        
        newNode.next = None
        
        return newhead
        

        