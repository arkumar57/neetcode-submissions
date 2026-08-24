# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head is None:

            return None
        
        curr = head

        count = 1
        
        while curr.next is not None:

            count += 1

            curr = curr.next
        
        print("count")
        print(count)
        if count == 1:

            return None
        
        target = count - n

        print("target")
        print(target)

        curr = head

        if target == 0:
            
            to_be_removed = curr

            curr = curr.next

            return curr

        while target > 1:

            target -= 1

            curr = curr.next
        
        to_be_removed = curr.next

        print(to_be_removed)
        # if to_be_removed is None:
        #     return head

        if to_be_removed.next is None:

            curr.next = None
        
        else:

            curr.next = to_be_removed.next

        return head

    



    
        