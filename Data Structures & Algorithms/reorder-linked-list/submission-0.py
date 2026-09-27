# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        second_part = slow.next
        slow.next = None

        prev_node = None
        while second_part:
            curent_next = second_part.next
            second_part.next = prev_node
            prev_node = second_part
            second_part = curent_next 

        n1 = head
        n2 = prev_node

        while n2:
            n1_next = n1.next
            n2_next = n2.next
    
            n1.next = n2
            n2.next = n1_next
    
            n1 = n1_next
            n2 = n2_next