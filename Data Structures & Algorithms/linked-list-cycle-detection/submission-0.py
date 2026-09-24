# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curent_node = head
        already_was = set()


        while curent_node:
            if curent_node in already_was:
                return True
            else:
                already_was.add(curent_node)
            curent_node = curent_node.next
        
        return False