# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        curr_l1 = l1
        curr_l2 = l2
        
        first_val = curr_l1.val + curr_l2.val
        head = ListNode(first_val % 10)
        curr = head
        carry = first_val // 10
        curr_l1 = curr_l1.next
        curr_l2 = curr_l2.next

        while curr_l1 and curr_l2:
            curr.next = ListNode()
            curr = curr.next
            val = curr_l1.val + curr_l2.val + carry
            curr.val = val % 10
            carry = val // 10
            curr_l1 = curr_l1.next
            curr_l2 = curr_l2.next

        while curr_l1:
            curr.next = ListNode()
            curr = curr.next
            val = curr_l1.val + carry
            curr.val = val % 10
            carry = val // 10
            curr_l1 = curr_l1.next

        while curr_l2:
            curr.next = ListNode()
            curr = curr.next
            val = curr_l2.val + carry
            curr.val = val % 10
            carry = val // 10
            curr_l2 = curr_l2.next

        if carry:
            curr.next = ListNode(1)
        return head