# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ln = 0
        curr = head
        while curr:
            ln += 1
            curr = curr.next
        prev = None
        curr = head

        for _ in range(ln - n):
            prev = curr
            curr = curr.next
        
        if prev == None:
            return curr.next
        
        prev.next = curr.next
        return head