# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        orders = []
        if not root:
            return orders
        q.append((root,0))

        while q:
            node, level = q.popleft()
            if len(orders) - 1 != level:
                orders.append([])
            orders[level].append(node.val)
            if node.left: q.append((node.left, level + 1))
            if node.right: q.append((node.right, level + 1))

        return orders