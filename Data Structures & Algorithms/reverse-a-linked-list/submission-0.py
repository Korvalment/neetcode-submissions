# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curent_node = head

        while curent_node is not None:
            next = curent_node.next 
            curent_node.next = prev
            prev = curent_node
            curent_node = next

        return prev