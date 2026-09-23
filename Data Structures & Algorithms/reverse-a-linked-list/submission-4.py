# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        curent_node = head

        while curent_node:
            next_node = curent_node.next
            curent_node.next = prev_node
            prev_node = curent_node
            curent_node = next_node
      
        return prev_node