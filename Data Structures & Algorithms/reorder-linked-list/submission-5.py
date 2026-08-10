# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head is None or head.next is None:

            return None

        count = 0

        curr = head

        while curr.next is not None:

            count += 1

            curr = curr.next
        

        division_point = count // 2

        if count % 2 == 0:

            division_point -= 1
        



        curr = head

        while division_point != 0:

            curr = curr.next

            division_point -= 1
        
        l2 = curr.next

        curr.next = None


        prev = None
        current = l2

        while current is not None:

            next_node = current.next

            current.next = prev

            prev = current

            current = next_node
        
        l2 = prev


        while head and l2 is not None:

            next1 = head.next
            next2 = l2.next

            head.next = l2

            if next1:

                l2.next = next1
            
            else:

                l2.next = next2

                break
        
            head = next1

            l2 = next2








    



        