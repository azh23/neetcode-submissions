"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        items = dict()

        og_curr = head
        dummy = Node(0)
        curr = dummy

        while og_curr:
            curr.next = Node(og_curr.val)
            curr = curr.next
            items[og_curr] = curr
            og_curr = og_curr.next

        new_head = dummy.next
        og_curr = head
        curr = new_head

        while og_curr:
            if og_curr.random:
                curr.random = items[og_curr.random]
            og_curr = og_curr.next
            curr = curr.next

        return new_head

