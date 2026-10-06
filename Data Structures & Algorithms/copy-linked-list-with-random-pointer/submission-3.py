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
        items = { None: None}
        og_curr = head

        while og_curr:
            copy = Node(og_curr.val)
            items[og_curr] = copy
            og_curr = og_curr.next

        og_curr = head

        while og_curr:
            copy = items[og_curr]
            copy.next = items[og_curr.next]
            copy.random = items[og_curr.random]
            og_curr = og_curr.next

        return items[head]

